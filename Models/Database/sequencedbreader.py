from Models.Database.idbconnection import *
from Models.sequence import Sequence
from typing import List, Dict
from Models.Database.seqTableCreator import *
from Models.dnaSequence import DNASequence


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
                # sequence = DNASequence("", "")
                seqMap = dict()
                for i in range(0, record.count()):
                    self.mapColToSequenceField(record.field(i), seqMap)
                seqs.append(seqMap)
            self._conn.close()
        return seqs

    def checkIfExists(self, where: str):
        if where == "" or where is None:
            return False
        sql = f"select 1 from {SequencesTableCreator.TABLE_NAME} where {where}"
        query = self._conn.createQuery(sql)
        if self._conn.executeQuery(query):
            if query.next():
                return True
        return False

    def __bindQuery(self, query, cols):
        for i in range(0, len(cols)):
            query.bindValue(i, cols[i])

    @classmethod
    def mapColToSequenceField(cls, col, seqMap: dict):
        if col.name() == SequencesTableCreator.ID_COL_NAME:
            seqMap[SequencesTableCreator.ID_COL_NAME] = col.value()
        elif col.name() == SequencesTableCreator.SEQ_COL_NAME:
            seqMap[SequencesTableCreator.SEQ_COL_NAME] = col.value()





