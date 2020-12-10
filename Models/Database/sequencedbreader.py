from idbconnection import *
from sequence import Sequence
from typing import List
from seqTableCreator import *


class SequenceDBReader:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def read(self, cols: List[str], where: str):
        marks=[]
        for c in cols:
            marks.append("?")

        sql = f"select {', '.join(marks)} from {SequencesTableCreator.TABLE_NAME()}"
        if where != "" and where is not None:
            sql += " where ?"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, cols)
        if where != "" and where is not None:
            query.bindValue(len(cols), where)
        return self._conn.executeQuery(query)

    def __bindQuery(self, query, cols):
        for i in range(0, len(cols)):
            query.bindValue(i, cols[i])




