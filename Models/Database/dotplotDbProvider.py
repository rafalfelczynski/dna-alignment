from typing import List
from Models.Database.idbconnection import IDBConnection
from Models.dotplot import Dotplot
from Models.sequence import Sequence
from Models.idotplotProvider import IDotplotProvider
from Models.Database.sequenceDbProvider import SequenceDbProvider


class DotplotDbProvider(IDotplotProvider):

    TABLE_NAME = "dotplots"
    SEQ1_ID_COL_NAME = "seq1_id"
    SEQ2_ID_COL_NAME = "seq2_id"
    DOTPLOT_COL_NAME = "dotplot"

    def __init__(self, dbConn: IDBConnection):
        self._conn: IDBConnection = dbConn

    def createTable(self):
        sql = f"create table if not exists {self.TABLE_NAME} (" \
              f" {self.SEQ1_ID_COL_NAME} text not null," \
              f" {self.SEQ2_ID_COL_NAME} text not null," \
              f" {self.DOTPLOT_COL_NAME} text not null," \
              f" primary key({self.SEQ1_ID_COL_NAME}, {self.SEQ2_ID_COL_NAME})," \
              f" foreign key({self.SEQ1_ID_COL_NAME}) references {SequenceDbProvider.TABLE_NAME}({SequenceDbProvider.ID_COL_NAME}) on delete cascade," \
              f" foreign key({self.SEQ2_ID_COL_NAME}) references {SequenceDbProvider.TABLE_NAME}({SequenceDbProvider.ID_COL_NAME}) on delete cascade)"
        query = self._conn.createQuery(sql)
        return self._conn.executeQuery(query)

    def read(self, id1, id2) -> List[Dotplot]:
        sql = f"select dot.{self.SEQ1_ID_COL_NAME}," \
              f" dot.{self.SEQ2_ID_COL_NAME}," \
              f" s1.{SequenceDbProvider.SEQ_COL_NAME} as seq1," \
              f" s2.{SequenceDbProvider.SEQ_COL_NAME} as seq2," \
              f" dot.{self.DOTPLOT_COL_NAME}" \
              f" from {self.TABLE_NAME} dot" \
              f" inner join {SequenceDbProvider.TABLE_NAME} s1 " \
              f"on s1.{SequenceDbProvider.ID_COL_NAME} = dot.{self.SEQ1_ID_COL_NAME}" \
              f" inner join {SequenceDbProvider.TABLE_NAME} s2 " \
              f"on s2.{SequenceDbProvider.ID_COL_NAME} = dot.{self.SEQ2_ID_COL_NAME}"
        if bool(id1) and bool(id2):
            sql += f' where {self.SEQ1_ID_COL_NAME} = ? and {self.SEQ2_ID_COL_NAME} = ?'
        query = self._conn.createQuery(sql)
        if bool(id1) and bool(id2):
            self._bindQuery(query, [id1, id2], 0)
        return self._readDotplots(query)

    def readAll(self):
        return self.read(None, None)

    def listAll(self):
        sql = f"select {self.SEQ1_ID_COL_NAME}," \
              f" {self.SEQ2_ID_COL_NAME}" \
              f" from {self.TABLE_NAME}"
        query = self._conn.createQuery(sql)
        return self._readDotplots(query)

    def _readDotplots(self, query):
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

    def _parseRecordMap(self, recordMap) -> Dotplot:
        seq1Id = recordMap[self.SEQ1_ID_COL_NAME]
        seq2Id = recordMap[self.SEQ2_ID_COL_NAME]
        dotplotMatrix = recordMap[self.DOTPLOT_COL_NAME] if self.DOTPLOT_COL_NAME in recordMap else None
        seq1 = recordMap["seq1"] if "seq1" in recordMap else ""
        seq2 = recordMap["seq2"] if "seq2" in recordMap else ""
        dotplot = Dotplot(Sequence(seq1Id, seq1), Sequence(seq2Id, seq2))
        if dotplotMatrix is not None and bool(seq1) and bool(seq2):
            try:
                dotplot.matrixFromString(dotplotMatrix, len(seq1), len(seq2))
            except ValueError as err:
                print("Error parsing matrix from string")
        return dotplot

    def delete(self, seq1id, seq2id) -> bool:
        sql = f"delete from {self.TABLE_NAME}" \
              f" where {self.SEQ1_ID_COL_NAME} = ?" \
              f" and {self.SEQ2_ID_COL_NAME} = ?"
        query = self._conn.createQuery(sql)
        self._bindQuery(query, [seq1id, seq2id], 0)
        return self._conn.executeQuery(query)

    def write(self, dotplot: Dotplot):
        sql = f"insert into {self.TABLE_NAME}({self.SEQ1_ID_COL_NAME}, " \
              f"{self.SEQ2_ID_COL_NAME}, " \
              f"{self.DOTPLOT_COL_NAME}) values(?, ?, ?)"
        query = self._conn.createQuery(sql)
        self._bindQuery(query, [dotplot.seq1.identifier, dotplot.seq2.identifier, dotplot.matrixToString()], 0)
        wasSuccessful = self._conn.executeQuery(query)
        return wasSuccessful

    def _bindQuery(self, query, values, startInd):
        for i in range(startInd, len(values)+startInd):
            query.bindValue(i, values[i-startInd])





