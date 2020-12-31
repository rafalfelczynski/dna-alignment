import sys
from Models.Database.seqReader import SeqDBReader
from Models.Database.dbconnection import DBConnection
from Models.dotplot import Dotplot
from Models.Database.dotplotDBWriter import DotplotDBWriter

DOTPLOT_PROGRAM_PATH = "Models/dotplotProgram.py"
DOTPLOT_PROGRAM_EXE_PATH = "dotplotProgram.exe"


def splitArgs(args):
    return ' '.join(args).split("$$$")


if __name__ == "__main__":
    try:
        args = splitArgs(sys.argv)
        if len(args) > 2:
            idSeq1 = args[1]
            idSeq2 = args[2]
            dbConn = DBConnection()
            seqDbReader = SeqDBReader(dbConn)
            seq1 = seqDbReader.readSeq(idSeq1)
            seq2 = seqDbReader.readSeq(idSeq2)
            if seq1.isNotEmpty() and seq2.isNotEmpty():
                dotplot = Dotplot(seq1, seq2)
                dotplot = dotplot.create()
                dotplotDbWriter = DotplotDBWriter(dbConn)
                succ = dotplotDbWriter.write(dotplot)
    except Exception as e:
        with open("log2.txt", "w+", encoding="utf-8") as f:
            [f.write(arg + "\n") for arg in splitArgs(sys.argv)]
            f.write(str(e))









