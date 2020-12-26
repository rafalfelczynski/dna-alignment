from Models.Database.idbconnection import *
from Models.sequence import Sequence
from Models.Database.seqTableCreator import *


class SequenceDbWriter:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def write(self, seq: Sequence):
        sql = f"insert into {SequencesTableCreator.TABLE_NAME}({SequencesTableCreator.ID_COL_NAME}, {SequencesTableCreator.SEQ_COL_NAME}) values(?, ?)"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, seq)
        return self._conn.executeQuery(query)

    def __bindQuery(self, query: QSqlQuery, seq: Sequence):
        query.bindValue(0, seq.identifier)
        query.bindValue(1, seq.sequence)



