from Models.Database.seqTableCreator import *
from Models.sequence import Sequence


class SequenceDbWriter:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def write(self, seq: Sequence):
        sql = f"insert into {SequencesTableCreator.TABLE_NAME}(" \
              f" {SequencesTableCreator.ID_COL_NAME}," \
              f" {SequencesTableCreator.SEQ_COL_NAME}," \
              f" {SequencesTableCreator.COMMENT_COL_NAME}) values(?, ?, ?)"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, seq)
        wasSuccessful = self._conn.executeQuery(query)
        self._conn.close()
        return wasSuccessful

    def __bindQuery(self, query: QSqlQuery, seq: Sequence):
        query.bindValue(0, seq.identifier)
        query.bindValue(1, seq.sequence)
        query.bindValue(2, seq.comment)



