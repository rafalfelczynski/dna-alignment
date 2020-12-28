from Models.iseqreader import ISeqReader
from Models.iseqwriter import ISeqWriter
from Models.sequence import Sequence
from PySide2.QtCore import QObject, Signal
from PySide2.QtNetwork import QNetworkAccessManager
from Models.networkFastaFetcher import NetworkFastaFetcher
from typing import List, Dict
from Views.infoDialog import *
from Views.confirmDialog import ConfirmDialog
from Models.isequpdater import ISeqUpdater


class SeqManager(QObject):

    new_seq_available = Signal(str)
    seq_already_exists = Signal(str)
    not_dna_sequence = Signal(str)
    seq_removed = Signal(str)

    def __init__(self, networkManager: QNetworkAccessManager, seqReader: ISeqReader, seqWriter: ISeqWriter, seqUpdater: ISeqUpdater):
        super().__init__()
        self._seqReader = seqReader
        self._seqWriter = seqWriter
        self._networkManager = networkManager
        self._fastaFetcher = NetworkFastaFetcher(self._networkManager)
        self._fastaFetcher.error_occurred.connect(self._networkErrorOccurred)
        self._fastaFetcher.data_ready.connect(self._seqFetched)
        self.dialogs = dict()
        self._seqUpdater = seqUpdater

    def getNewSeqFromNet(self, seqId):
        # Check if sequence already exists
        if self._seqReader.checkIfExists(seqId):
            self.seq_already_exists.emit(seqId)
        else:
            # Set new task for retrieving sequence from the internet
            self._fastaFetcher.fetchFasta(seqId)

    def showSequence(self, seqId):
        sequence = self._seqReader.readSeq(seqId)
        if sequence.isNotEmpty():
            self.addDialogWithSequence(sequence)

    def removeSequence(self, seqId):
        dialog = ConfirmDialog()
        dialog.setText(f"Are you sure you want to remove this sequence?\n"
                       f"It will also REMOVE EVERY RELATED dotplot and alignment\n"
                       f"Sequence Id: \n{seqId}")
        dialog.resize(400, 200)
        dialog.accepted.connect(lambda: self._removeSequenceFromDb(seqId))
        dialog.exec_()

    def _removeSequenceFromDb(self, seqId):
        if self._seqUpdater.deleteSeq(seqId):
            self.seq_removed.emit(seqId)
        else:
            dialog = InfoDialog()
            dialog.setText("Sequence was not removed! Error with database occurred!")
            dialog.exec_()

    def addDialogWithSequence(self, sequence):
        dialog = InfoDialog()
        self.dialogs[dialog.identifier] = dialog
        dialog.finished.connect(lambda: self.removeDialogWithSequence(dialog.identifier))
        dialog.setText(f"Identifier:\n{sequence.identifier}\n\nSequence:\n{sequence.cutSequenceIntoFragments(50)}")
        dialog.resize(600, 300)
        dialog.setWindowModality(Qt.NonModal)
        dialog.show()

    def removeDialogWithSequence(self, identifier):
        if identifier in self.dialogs:
            self.dialogs.pop(identifier)

    def getAllSeqs(self) -> List[Sequence]:
        return self._seqReader.readAll()

    def _networkErrorOccurred(self, msg):
        dialog = InfoDialog()
        dialog.setText(msg)
        dialog.exec_()

    def _seqFetched(self, id: str, seq: str):
        if id and seq:
            sequence = Sequence(id, seq)
            if sequence.isValid():
                if self.addSeqToDatabase(sequence):
                    self.new_seq_available.emit(id)
                else:
                    self.seq_already_exists.emit(id)
                    dialog = InfoDialog()
                    dialog.resize(300, 200)
                    dialog.setText(f'Sequence with the id "{id}" already exists!')
                    dialog.exec_()
            else:
                self.not_dna_se.emit(id)
        else:
            self.not_dna_se.emit(id)

    def addSeqToDatabase(self, sequence: Sequence):
        if sequence.isValid():
            return self._seqWriter.writeSeq(sequence)
        else:
            return False









