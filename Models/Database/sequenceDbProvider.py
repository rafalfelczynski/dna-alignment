from typing import List
from Models.Database.idbconnection import IDBConnection
from Models.sequence import Sequence
from Models.isequenceProvider import ISequenceProvider


class SequenceDbProvider(ISequenceProvider):

    TABLE_NAME = "sequences"
    ID_COL_NAME = "id"
    SEQ_COL_NAME = "sequence"
    COMMENT_COL_NAME = "comment"

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def createTable(self):
        sql = f"create table if not exists {self.TABLE_NAME}(" \
              f"{self.ID_COL_NAME} text primary key," \
              f" {self.SEQ_COL_NAME} text not null," \
              f" {self.COMMENT_COL_NAME} text)"
        query = self._conn.createQuery(sql)
        return self._conn.executeQuery(query)

    def read(self, ident) -> List[Sequence]:
        sql = f"select {self.ID_COL_NAME}, {self.SEQ_COL_NAME}, {self.COMMENT_COL_NAME} from {self.TABLE_NAME}"
        if ident != "" and ident is not None:
            sql += f' where {self.ID_COL_NAME} = ?'
        query = self._conn.createQuery(sql)
        if ident != "" and ident is not None:
            self._bindQuery(query, [ident], 0)
        seqs = []
        if self._conn.executeQuery(query):
            while query.next():
                record = query.record()
                seqMap = dict()
                for i in range(0, record.count()):
                    field = record.field(i)
                    seqMap[field.name()] = field.value()
                seqs.append(self._fetchOneSequence(seqMap))
        self._conn.close()
        return seqs

    def readAll(self) -> List[Sequence]:
        return self.read(None)

    def checkIfExists(self, where: str):
        if where == "" or where is None:
            return False
        sql = f"select 1 from {self.TABLE_NAME} where {where}"
        query = self._conn.createQuery(sql)
        exists = False
        if self._conn.executeQuery(query):
            if query.next():
                exists = True
        self._conn.close()
        return exists

    def delete(self, ident: str):
        sql = f'delete from {self.TABLE_NAME} where {self.ID_COL_NAME} = ?'
        query = self._conn.createQuery(sql)
        self._bindQuery(query, [ident], 0)
        wasSuccessful = self._conn.executeQuery(query)
        self._conn.close()
        return wasSuccessful

    def write(self, seq: Sequence):
        sql = f"insert into {self.TABLE_NAME}(" \
              f" {self.ID_COL_NAME}," \
              f" {self.SEQ_COL_NAME}," \
              f" {self.COMMENT_COL_NAME}) values(?, ?, ?)"
        query = self._conn.createQuery(sql)
        self._bindQuery(query, [seq.identifier, seq.sequence, seq.comment], 0)
        wasSuccessful = self._conn.executeQuery(query)
        self._conn.close()
        return wasSuccessful

    def _bindQuery(self, query, values, startIndex):
        for i in range(startIndex, len(values)+startIndex):
            query.bindValue(i, values[i-startIndex])

    def _fetchOneSequence(self, seqMap):
        id = seqMap[self.ID_COL_NAME]
        sequence = seqMap[self.SEQ_COL_NAME]
        comment = seqMap[self.COMMENT_COL_NAME]
        return Sequence(id, sequence, comment)







