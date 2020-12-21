from Views.ui_infodialog import *


class InfoDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def setText(self, text: str):
        self.ui.textEdit.setPlainText(text)


