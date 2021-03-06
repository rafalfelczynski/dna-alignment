from Views.insertTextDialog import *
from Views.infoDialog import *
from Models.sequenceManager import SeqManager


class SeqDialogController(QObject):

    def __init__(self, seqStorage: SeqManager):
        super().__init__()
        self._dialog: InsertTextDialog = ...
        self._seqManager = seqStorage

    def showDialog(self):
        self._dialog = InsertTextDialog()
        self._dialog.setFocus()
        self._dialog.text_inserted.connect(self._okBtnClicked)
        self._dialog.rejected.connect(self._cancelBtnClicked)
        self._dialog.exec_()

    def _okBtnClicked(self, seqId):
        self._seqManager.getNewSeqFromNet(seqId)

    def _cancelBtnClicked(self):
        pass













