from Views.ui_confirmdialog import *


class ConfirmDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def setText(self, text: str):
        self.ui.plainTextEdit.setPlainText(text)








