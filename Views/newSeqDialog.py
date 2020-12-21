from Views.ui_newseqdialog import *


class NewSeqDialog(QDialog):

    identifier_inserted = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_NewSequence()
        self.ui.setupUi(self)

    def accept(self) -> None:
        super().accept()
        self.identifier_inserted.emit(self.ui.identifierLineEdit.text())










