from PySide2.QtWidgets import QWidget
from ui_mainwindow import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)