import sys
from Controllers.controller import *
from Controllers.processController import *
from Views.fileDropAcceptor import *
from Models.Database.alignmentReader import AlignmentReader
from Models.alignment import Alignment
import numpy as np


def main():
    # con = DBConnection()
    # a = AlignmentReader(con)
    # ali = a.readAllAlignments()
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    contr = Controller()
    contr.finished.connect(app.quit)
    return sys.exit(app.exec_())


if __name__ == "__main__":
    main()
