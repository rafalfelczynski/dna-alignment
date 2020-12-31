from Models.Database.idbconnection import *
from Models.Database.alignmentTableCreator import AlignmentTableCreator


class AlignmentDbDeleterWorker:

    def __init__(self, dbConn: IDBConnection):
        self._dbconn = dbConn

    def delete(self, seq1id, seq2id, match, mismatch, gap) -> bool:
        sql = f"delete from {AlignmentTableCreator.TABLE_NAME}" \
              f" where {AlignmentTableCreator.SEQ1_ID_COL_NAME} = ?" \
              f" and {AlignmentTableCreator.SEQ2_ID_COL_NAME} = ?" \
              f" and {AlignmentTableCreator.MATCH_COL_NAME} = ?" \
              f" and {AlignmentTableCreator.MISMATCH_COL_NAME} = ?" \
              f" and {AlignmentTableCreator.GAP_COL_NAME} = ?"
        query = self._dbconn.createQuery(sql)
        self.__bindQuery(query, [seq1id, seq2id, match, mismatch, gap], 0)
        return self._dbconn.executeQuery(query)

    def __bindQuery(self, query, values, startInd):
        for i in range(startInd, len(values)+startInd):
            query.bindValue(i, values[i-startInd])


