from idbconnection import *
from sequence import Sequence
from typing import List
from seqTableCreator import *
from dnaSequence import DNASequence


class SequenceDBReader:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def read(self, cols: List[str], where: str):
        sql = f"select {','.join(cols)} from {SequencesTableCreator.TABLE_NAME}"
        if where != "" and where is not None:
            sql += f" where {where}"
        query = self._conn.createQuery(sql)
        seqs = []
        if self._conn.executeQuery(query):
            while query.next():
                record = query.record()
                sequence = DNASequence("", "")
                print("record count:", record.count(), record.field(0).name(), "sql:", query.lastQuery(), cols)
                for i in range(0, record.count()):
                    self.mapColToSequenceField(record.field(i), sequence)
                seqs.append(sequence)
            self._conn.close()
        return seqs


    def __bindQuery(self, query, cols):
        for i in range(0, len(cols)):
            query.bindValue(i, cols[i])

    def mapColToSequenceField(self, col, seq: Sequence):
        if col.name() == SequencesTableCreator.ID_COL_NAME:
            seq.identifier = col.value()
        elif col.name() == SequencesTableCreator.SEQ_COL_NAME:
            seq.sequence = col.value()





