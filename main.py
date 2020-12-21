import sys
from Controllers.controller import *
from Controllers.processController import *


def main():
    global cnt, start
    app = QApplication([])
    procContr = ProcessController()
    contr = Controller(procContr)
    return sys.exit(app.exec_())


if __name__ == "__main__":
    main()
