from Models.iseqreader import ISeqReader
from Models.Database.sequencedbreader import SequenceDbReader
from Models.Database.idbconnection import IDBConnection
from Models.Database.seqTableCreator import SequencesTableCreator


class SeqDBReader(ISeqReader):

    def __init__(self, dbConn: IDBConnection):
        self._reader = SequenceDbReader(dbConn)
        pass

    def readSeq(self, id):
        return self._reader.read([SequencesTableCreator.ID_COL_NAME, SequencesTableCreator.SEQ_COL_NAME],
                                 f" {SequencesTableCreator.ID_COL_NAME} = {id}")

    def readAll(self):
        return self._reader.read(["*"], None)

    def checkIfExists(self, id):
        return self._reader.checkIfExists(f"{SequencesTableCreator.ID_COL_NAME} = {id}")










