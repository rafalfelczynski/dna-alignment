import sys
from PySide2.QtWidgets import QApplication
from Controllers.controller import Controller


def main():
    app = QApplication([])
    app.setApplicationName("DNA Alignment")
    app.setQuitOnLastWindowClosed(False)
    contr = Controller()
    contr.finished.connect(app.quit)
    return sys.exit(app.exec_())


if __name__ == "__main__":
    main()
