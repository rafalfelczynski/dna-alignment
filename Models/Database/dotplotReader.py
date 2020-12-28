from Models.Database.dotplotDbReader import *
from Models.dotplot import Dotplot
from typing import List


class DotplotReader:

    def __init__(self, dbConn: IDBConnection):
        self._reader = DotplotDbReader(dbConn)

    def readDotplot(self, seq1Id, seq2Id) -> Dotplot:
        recordMaps = self._reader.readDotplot(f"{DotplotTableCreator.SEQ1_COL_NAME} = ?"
                                              f" and {DotplotTableCreator.SEQ2_COL_NAME} = ?", [seq1Id, seq2Id])
        if len(recordMaps) > 0:
            return self._parseRecordMap(recordMaps[0])
        return Dotplot(None, None)

    def readAllDotplots(self) -> List[Dotplot]:
        recordMaps = self._reader.readDotplot(where=None, whereValues=None)
        dotplots = []
        for recordMap in recordMaps:
            dotplots.append(self._parseRecordMap(recordMap))
        return dotplots

    def _parseRecordMap(self, recordMap) -> Dotplot:
        seq1Id = recordMap[DotplotTableCreator.SEQ1_COL_NAME]
        seq2Id = recordMap[DotplotTableCreator.SEQ2_COL_NAME]
        dotplotMatrix = recordMap[DotplotTableCreator.DOTPLOT_COL_NAME]
        seq1 = recordMap[SequencesTableCreator.SEQ_COL_NAME]
        seq2 = recordMap[SequencesTableCreator.SEQ_COL_NAME]
        dotplot = Dotplot(Sequence(seq1Id, seq1), Sequence(seq2Id, seq2))
        dotplot.matrixFromString(dotplotMatrix, len(seq1), len(seq2))
        return dotplot





