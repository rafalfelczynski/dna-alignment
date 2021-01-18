import sys
import PySide2
from Models.Database.dotplotRepository import *
from Models.Database.dotplotDbProvider import *
from Models.Database.dbconnection import DBConnection
from Models.Database.sequenceRepository import *
from Models.Database.sequenceDbProvider import *
from Models.dotplot import Dotplot

DOTPLOT_PROGRAM_PATH = "Models/dotplotProgram.py"
DOTPLOT_PROGRAM_EXE_PATH = "dotplotProgram.exe"


def splitArgs(args):
    return ' '.join(args).split("$$$")


if __name__ == "__main__":
    try:
        with open("log2.txt", "w+", encoding="utf-8") as f:
            args = splitArgs(sys.argv)
            if len(args) > 2:
                idSeq1 = args[1]
                idSeq2 = args[2]

                f.write("before connected\n")
                dbConn = DBConnection()
                f.write("after connect\n")
                seqRepo = SequenceRepository(SequenceDbProvider(dbConn))

                f.write("repo created\n")
                seq1 = seqRepo.readSeq(idSeq1)
                seq2 = seqRepo.readSeq(idSeq2)
                f.write("seq1, seq2\n" + seq1.sequence + " " + seq2.sequence)
                if seq1.isNotEmpty() and seq2.isNotEmpty():
                    dotplot = Dotplot(seq1, seq2)
                    dotplot = dotplot.create()
                    dotplotRepo = DotplotRepository(DotplotDbProvider(dbConn))
                    succ = dotplotRepo.writeDotplot(dotplot)
    except Exception as e:
        with open("log3.txt", "w+", encoding="utf-8") as f:
            [f.write(arg + "\n") for arg in splitArgs(sys.argv)]
            f.write(str(e))









