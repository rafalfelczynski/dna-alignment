from Views.ui_infodialog import *


class InfoDialog(QDialog):

    __IDENTIFIER = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.identifier = InfoDialog.__IDENTIFIER
        InfoDialog.__IDENTIFIER += 1

    def setText(self, text: str):
        self.ui.textEdit.setPlainText(text)


