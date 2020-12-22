import sys
from Controllers.controller import *
from Controllers.processController import *
from Views.fileDropAcceptor import *


def main():
    global cnt, start
    app = QApplication([])
    # app.setQuitOnLastWindowClosed(False)
    # procContr = ProcessController()
    # contr = Controller(procContr)
    # contr.finished.connect(app.quit)
    f = FileDropAcceptor()
    f.show()
    print("".join(["ala", "ma", "kota"]))
    return sys.exit(app.exec_())


if __name__ == "__main__":
    main()
