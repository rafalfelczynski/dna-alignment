from typing import List
from Models.Database.alignmentDbReader import *
from Models.scoring import Scoring
from Models.sequence import Sequence
from Models.alignment import Alignment


class AlignmentReader:

    def __init__(self, dbConn: IDBConnection):
        self._reader: AlignmentDbReader = AlignmentDbReader(dbConn)

    def readAlignment(self, seq1Id, seq2Id, scoring: Scoring) -> Alignment:
        alignments = self._reader.read(f"{AlignmentTableCreator.SEQ1_ID_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.SEQ2_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.MATCH_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.MISMATCH_COL_NAME} = ?"
                                          f" and {AlignmentTableCreator.GAP_COL_NAME} = ?", [seq1Id, seq2Id, scoring.match, scoring.mismatch, scoring.gap])
        if len(alignments) > 0:
            return alignments[0]
        return Alignment()

    def readAllAlignments(self):
        alignments = self._reader.read(None, None)
        return alignments



