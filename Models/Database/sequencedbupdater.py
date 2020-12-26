from Models.Database.idbconnection import *
from Models.Database.seqTableCreator import *


class SequenceDbUpdater:

    def __init__(self, dbConn: IDBConnection):
        self._conn = dbConn

    def delete(self, id: str):
        sql = f'delete from {SequencesTableCreator.TABLE_NAME} where {SequencesTableCreator.ID_COL_NAME} = "{id}"'
        query = self._conn.createQuery(sql)
        wasSuccessful = self._conn.executeQuery(query)
        self._conn.close()
        return wasSuccessful




