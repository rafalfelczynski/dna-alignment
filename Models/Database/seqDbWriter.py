from Models.iseqwriter import ISeqWriter
from Models.Database.sequencedbwriter import SequenceDbWriter
from Models.Database.idbconnection import IDBConnection
from Models.sequence import Sequence


class SeqDBWriter(ISeqWriter):

    def __init__(self, dbConn: IDBConnection):
        self._reader = SequenceDbWriter(dbConn)
        pass

    def writeSeq(self, seq: Sequence):
        return self._reader.write(seq)










