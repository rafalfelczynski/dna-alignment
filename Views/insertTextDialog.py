from Views.ui_newseqdialog import *


class InsertTextDialog(QDialog):

    text_inserted = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_NewSequence()
        self.ui.setupUi(self)
        self.resize(250, 120)

    def setEditFieldTitle(self, title):
        self.ui.label.setText(title)

    def setEditFieldText(self, text):
        self.ui.identifierLineEdit.setText(text)
        self.ui.identifierLineEdit.setFocus()

    def accept(self) -> None:
        super().accept()
        self.text_inserted.emit(self.ui.identifierLineEdit.text())










