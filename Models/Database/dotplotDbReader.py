from Models.Database.sequencedbreader import SequenceDbReader
from Models.Database.idbconnection import IDBConnection
from Models.Database.seqTableCreator import SequencesTableCreator
from Models.Database.dotplotTableCreator import DotplotTableCreator
from typing import List, Dict
from Models.sequence import Sequence


class DotplotDbReader:

    def __init__(self, dbConn: IDBConnection):
        self._conn: IDBConnection = dbConn

    def readDotplot(self, where=None, whereValues=None) -> List[Dict[str, str]]:
        sql = f"select dot.{DotplotTableCreator.SEQ1_COL_NAME}," \
              f" dot.{DotplotTableCreator.SEQ2_COL_NAME}," \
              f" s1.{SequencesTableCreator.SEQ_COL_NAME}," \
              f" s2.{SequencesTableCreator.SEQ_COL_NAME}," \
              f" dot.{DotplotTableCreator.DOTPLOT_COL_NAME}" \
              f" from {DotplotTableCreator.TABLE_NAME} dot" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s1 " \
              f"on s1.{SequencesTableCreator.ID_COL_NAME} = dot.{DotplotTableCreator.SEQ1_COL_NAME}" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s2 " \
              f"on s2.{SequencesTableCreator.ID_COL_NAME} = dot.{DotplotTableCreator.SEQ2_COL_NAME} "
        if where is not None and where != "":
              sql += f'where {where}'
        query = self._conn.createQuery(sql)
        if where is not None and where != "":
            self._bindQuery(query, whereValues)
        dotplots = []
        if self._conn.executeQuery(query):
            while query.next():
                record = query.record()
                dotplotMap = dict()
                for i in range(0, record.count()):
                    field = record.field(i)
                    dotplotMap[field.name()] = field.value()
                dotplots.append(dotplotMap)
        self._conn.close()
        return dotplots

    def _bindQuery(self, query, values):
        for i in range(0, len(values)):
            query.bindValue(i, values[i])

    # def readAll(self) -> List[Sequence]:
    #     seqs = []
    #     for seqMap in self._reader.read(["*"], None):
    #         seqs.append(self._fetchOneSequence(seqMap))
    #     return seqs

    # def checkIfExists(self, id):
    #     return self._reader.checkIfExists(f'{SequencesTableCreator.ID_COL_NAME} = "{id}"')

    # def _fetchOneSequence(self, seqMap):
    #     id = seqMap[SequencesTableCreator.ID_COL_NAME]
    #     sequence = seqMap[SequencesTableCreator.SEQ_COL_NAME]
    #     return Sequence(id, sequence)




