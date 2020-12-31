from typing import List, Dict

from Models.Database.seqTableCreator import *


class SequenceDbReader:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def read(self, cols: List[str], where: str) -> List[Dict[str, str]]:
        sql = f"select {','.join(cols)} from {SequencesTableCreator.TABLE_NAME}"
        if where != "" and where is not None:
            sql += f" where {where}"
        query = self._conn.createQuery(sql)
        seqs = []
        if self._conn.executeQuery(query):
            while query.next():
                record = query.record()
                seqMap = dict()
                for i in range(0, record.count()):
                    field = record.field(i)
                    seqMap[field.name()] = field.value()
                seqs.append(seqMap)
        self._conn.close()
        return seqs

    def checkIfExists(self, where: str):
        if where == "" or where is None:
            return False
        sql = f"select 1 from {SequencesTableCreator.TABLE_NAME} where {where}"
        query = self._conn.createQuery(sql)
        exists = False
        if self._conn.executeQuery(query):
            if query.next():
                exists = True
        self._conn.close()
        return exists

    def __bindQuery(self, query, cols):
        for i in range(0, len(cols)):
            query.bindValue(i, cols[i])





