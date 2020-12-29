from typing import List
from Models.Database.alignmentDbReader import *
from Models.scoring import Scoring
from Models.sequence import Sequence
from Models.alignment import Alignment


class AlignmentReader:

    def __init__(self, dbConn: IDBConnection):
        self._reader: AlignmentDbReader = AlignmentDbReader(dbConn)

    def readAlignment(self, seq1Id, seq2Id, scoring: Scoring) -> Alignment:
        alignments = self._reader.readAlignment(f"{AlignmentTableCreator.SEQ1_ID_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.SEQ2_ID_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.MATCH_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.MISMATCH_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.GAP_COL_NAME} = ?", [seq1Id, seq2Id, scoring.match, scoring.mismatch, scoring.gap])
        if len(alignments) > 0:
            return alignments[0]
        return Alignment()

    def readAllAlignments(self) -> List[Alignment]:
        columnsToRead = [AlignmentTableCreator.SEQ1_ID_COL_NAME, AlignmentTableCreator.SEQ2_ID_COL_NAME,
                         AlignmentTableCreator.MATCH_COL_NAME,
                         AlignmentTableCreator.MISMATCH_COL_NAME,
                         AlignmentTableCreator.GAP_COL_NAME]
        recordMaps = self._reader.read(columnsToRead, where=None, whereValues=None)
        alignments = []
        for recordMap in recordMaps:
            values = self._parseRecordMap(recordMap, columnsToRead)
            seq1 = Sequence(values[0], None)
            seq2 = Sequence(values[1], None)
            scoring = Scoring(float(values[2]), float(values[3]), float(values[4]))
            alignments.append(Alignment(seq1, seq2, scoring))
        return alignments

    def _parseRecordMap(self, recordMap, cols) -> List[str]:
        results = [recordMap[col] for col in cols]
        return results

    def checkIfExists(self, seq1Id, seq2Id, scoring: Scoring):
        return self.readAlignment(seq1Id, seq2Id, scoring).isValid()






