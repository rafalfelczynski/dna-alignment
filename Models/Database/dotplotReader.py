from typing import List

from Models.Database.dotplotDbReader import *
from Models.Database.dotplotTableCreator import DotplotTableCreator
from Models.dotplot import Dotplot


class DotplotReader:

    def __init__(self, dbConn: IDBConnection):
        self._reader = DotplotDbReader(dbConn)

    def readDotplot(self, seq1Id, seq2Id) -> Dotplot:
        dotplots = self._reader.readDotplot(f"{DotplotTableCreator.SEQ1_COL_NAME} = ?"
                                              f" and {DotplotTableCreator.SEQ2_COL_NAME} = ?", [seq1Id, seq2Id])
        if len(dotplots) > 0:
            return dotplots[0]
        return Dotplot(None, None)

    def readAllDotplots(self) -> List[Dotplot]:
        columnsToRead = [DotplotTableCreator.SEQ1_COL_NAME, DotplotTableCreator.SEQ2_COL_NAME]
        recordMaps = self._reader.read(columnsToRead, where=None, whereValues=None)
        dotplots = []
        for recordMap in recordMaps:
            values = self._parseRecordMap(recordMap, columnsToRead)
            dotplots.append(Dotplot(Sequence(values[0], None), Sequence(values[1], None)))
        return dotplots

    def checkIfExists(self, seq1Id, seq2Id):
        columnsToRead = [DotplotTableCreator.SEQ1_COL_NAME, DotplotTableCreator.SEQ2_COL_NAME]
        recordMaps = self._reader.read(columnsToRead, f"{DotplotTableCreator.SEQ1_COL_NAME} = ?"
                                                      f" and {DotplotTableCreator.SEQ2_COL_NAME} = ?", [seq1Id, seq2Id])
        return len(recordMaps) > 0

    def _parseRecordMap(self, recordMap, cols) -> List[str]:
        results = [recordMap[col] for col in cols]
        return results





