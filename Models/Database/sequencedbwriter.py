from idbconnection import *
from sequence import Sequence
from seqTableCreator import *


class SequenceDbWriter:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def write(self, seq: Sequence):
        sql = f"insert into {SequencesTableCreator.TABLE_NAME()}(id, seq) values(?, ?)"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, seq)
        return self._conn.executeQuery(query)


    def __bindQuery(self, query: QSqlQuery, seq: Sequence):
        query.bindValues(0, seq.identifier)
        query.bindValues(1, seq.sequence)



