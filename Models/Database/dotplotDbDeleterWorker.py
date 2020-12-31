from Models.Database.idbconnection import *
from Models.Database.dotplotTableCreator import DotplotTableCreator


class DotplotDbDeleterWorker:

    def __init__(self, dbConn: IDBConnection):
        self._dbconn = dbConn

    def delete(self, seq1id, seq2id) -> bool:
        sql = f"delete from {DotplotTableCreator.TABLE_NAME}" \
              f" where {DotplotTableCreator.SEQ1_COL_NAME} = ?" \
              f" and {DotplotTableCreator.SEQ2_COL_NAME} = ?"
        query = self._dbconn.createQuery(sql)
        self.__bindQuery(query, [seq1id, seq2id], 0)
        return self._dbconn.executeQuery(query)

    def __bindQuery(self, query, values, startInd):
        for i in range(startInd, len(values)+startInd):
            query.bindValue(i, values[i-startInd])


