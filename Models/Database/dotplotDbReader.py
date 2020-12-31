from typing import List, Dict

from Models.Database.dotplotTableCreator import DotplotTableCreator
from Models.Database.idbconnection import IDBConnection
from Models.Database.seqTableCreator import SequencesTableCreator
from Models.dotplot import Dotplot
from Models.sequence import Sequence


class DotplotDbReader:

    def __init__(self, dbConn: IDBConnection):
        self._conn: IDBConnection = dbConn

    def readDotplot(self, where=None, whereValues=None) -> List[Dotplot]:
        sql = f"select dot.{DotplotTableCreator.SEQ1_COL_NAME}," \
              f" dot.{DotplotTableCreator.SEQ2_COL_NAME}," \
              f" s1.{SequencesTableCreator.SEQ_COL_NAME} as seq1," \
              f" s2.{SequencesTableCreator.SEQ_COL_NAME} as seq2," \
              f" dot.{DotplotTableCreator.DOTPLOT_COL_NAME}" \
              f" from {DotplotTableCreator.TABLE_NAME} dot" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s1 " \
              f"on s1.{SequencesTableCreator.ID_COL_NAME} = dot.{DotplotTableCreator.SEQ1_COL_NAME}" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s2 " \
              f"on s2.{SequencesTableCreator.ID_COL_NAME} = dot.{DotplotTableCreator.SEQ2_COL_NAME}"
        if where is not None and where != "":
              sql += f' where {where}'
        query = self._conn.createQuery(sql)
        if where is not None and where != "":
            self._bindQuery(query, whereValues, 0)
        dotplots = []
        if self._conn.executeQuery(query):
            while query.next():
                record = query.record()
                dotplotMap = dict()
                for i in range(0, record.count()):
                    field = record.field(i)
                    dotplotMap[field.name()] = field.value()
                dotplots.append(self._parseRecordMap(dotplotMap))
        self._conn.close()
        return dotplots

    def read(self, cols: List[str], where=None, whereValues=None) -> List[Dict[str, str]]:
        sql = f"select {','.join(cols)}" \
              f" from {DotplotTableCreator.TABLE_NAME} dot" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s1 " \
              f"on s1.{SequencesTableCreator.ID_COL_NAME} = dot.{DotplotTableCreator.SEQ1_COL_NAME}" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s2 " \
              f"on s2.{SequencesTableCreator.ID_COL_NAME} = dot.{DotplotTableCreator.SEQ2_COL_NAME}"
        if where is not None and where != "":
            sql += f' where {where}'
        query = self._conn.createQuery(sql)
        if where is not None and where != "":
            self._bindQuery(query, whereValues, 0)
        dotplots = []
        if self._conn.executeQuery(query):
            while query.next():
                record = query.record()
                dotplotMap = dict()
                for i in range(0, record.count()):
                    field = record.field(i)
                    dotplotMap[field.name()] = field.value()
                dotplots.append(dotplotMap)
        self._conn.close()
        return dotplots

    def _bindQuery(self, query, values, startIndex):
        for i in range(startIndex, len(values)+startIndex):
            query.bindValue(i, values[i])

    def _parseRecordMap(self, recordMap) -> Dotplot:
        seq1Id = recordMap[DotplotTableCreator.SEQ1_COL_NAME]
        seq2Id = recordMap[DotplotTableCreator.SEQ2_COL_NAME]
        dotplotMatrix = recordMap[DotplotTableCreator.DOTPLOT_COL_NAME]
        seq1 = recordMap["seq1"]
        seq2 = recordMap["seq2"]
        dotplot = Dotplot(Sequence(seq1Id, seq1), Sequence(seq2Id, seq2))
        try:
            dotplot.matrixFromString(dotplotMatrix, len(seq1), len(seq2))
        except ValueError as err:
            print(err)
        return dotplot




