from Models.iseqreader import ISeqReader
from Models.Database.sequencedbreader import SequenceDbReader
from Models.Database.idbconnection import IDBConnection
from Models.Database.seqTableCreator import SequencesTableCreator
from typing import List
from Models.sequence import Sequence


class SeqDBReader(ISeqReader):

    def __init__(self, dbConn: IDBConnection):
        self._reader = SequenceDbReader(dbConn)
        pass

    def readSeq(self, id) -> Sequence:
        readSeqs = self._reader.read([SequencesTableCreator.ID_COL_NAME,
                                      SequencesTableCreator.SEQ_COL_NAME,
                                      SequencesTableCreator.COMMENT_COL_NAME],
                                 f' {SequencesTableCreator.ID_COL_NAME} = "{id}"')
        if len(readSeqs) > 0:
            return self._fetchOneSequence(readSeqs[0])
        return Sequence("", "")

    def readAll(self) -> List[Sequence]:
        seqs = []
        for seqMap in self._reader.read(["*"], None):
            seqs.append(self._fetchOneSequence(seqMap))
        return seqs

    def checkIfExists(self, id):
        return self._reader.checkIfExists(f'{SequencesTableCreator.ID_COL_NAME} = "{id}"')

    def _fetchOneSequence(self, seqMap):
        id = seqMap[SequencesTableCreator.ID_COL_NAME]
        sequence = seqMap[SequencesTableCreator.SEQ_COL_NAME]
        comment = seqMap[SequencesTableCreator.COMMENT_COL_NAME]
        return Sequence(id, sequence, comment)










