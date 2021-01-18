import sys
from PySide2.QtWidgets import QApplication
from Controllers.controller import Controller

app = ...


def main():
    global app
    app = QApplication([])
    app.setApplicationName("DNA Alignment")
    app.setQuitOnLastWindowClosed(False)
    contr = Controller()
    contr.finished.connect(app.quit)
    app.exec_()


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print("error", e)
