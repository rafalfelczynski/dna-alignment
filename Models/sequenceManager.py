from Models.iseqreader import ISeqReader
from Models.iseqwriter import ISeqWriter
from Models.sequence import Sequence
from PySide2.QtCore import QObject, Signal
from PySide2.QtNetwork import QNetworkAccessManager
from Models.networkFastaFetcher import NetworkFastaFetcher
from typing import List, Dict


class SeqManager(QObject):

    new_seq_available = Signal(str)
    seq_already_exists = Signal(str)

    def __init__(self, networkManager: QNetworkAccessManager, seqReader: ISeqReader, seqWriter: ISeqWriter):
        super().__init__()
        self._seqReader = seqReader
        self._seqWriter = seqWriter
        self._networkManager = networkManager
        self._fastaFetcher = NetworkFastaFetcher(self._networkManager)
        self._fastaFetcher.error_occurred.connect(self._networkErrorOccurred)
        self._fastaFetcher.data_ready.connect(self._seqFetched)

    def getNewSeqFromNet(self, seqId):
        # Check if sequence already exists
        if self._seqReader.checkIfExists(seqId):
            # TODO: Notify that sequence already exists...
            pass
        else:
            # Set new task for retrieving sequence from the internet
            self._fastaFetcher.fetchFasta(seqId)

    def getAllSeqs(self) -> List[Dict[str, str]]:
        return self._seqReader.readAll()

    def _networkErrorOccurred(self, msg):
        print(msg)

    def _seqFetched(self, id: str, seq: str):
        if id and seq:
            if self._addSeqToDatabase(Sequence(id, seq)):
                self._notifyAboutNewSeq(id)
            else:
                self.seq_already_exists.emit(id)

    def _addSeqToDatabase(self, sequence: Sequence):
        self._seqWriter.writeSeq(sequence)
        pass

    def _notifyAboutNewSeq(self, id):
        self.new_seq_available.emit(id)









