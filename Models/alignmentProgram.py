import sys
from Models.Database.dotplotDBWriter import *
from Models.Database.seqDbWriter import *
from Models.Database.seqReader import SeqDBReader
from Models.Database.dbconnection import DBConnection
from Models.dnaDotplot import *
from Models.dotplotStorage import *


def splitArgs(args):
    return ' '.join(args).split("$$$")


if __name__ == "__main__":
    args = splitArgs(sys.argv)
    with open("log.txt", "w+", encoding="utf-8") as f:
        [f.write(arg + "\n") for arg in splitArgs(sys.argv)]
        if len(args) > 2:
            idSeq1 = args[1]
            idSeq2 = args[2]
            try:
                match = float(args[3])
                mismatch = float(args[4])
                gap = float(args[5])
                dbConn = DBConnection()
                seqDbReader = SeqDBReader(dbConn)
                seq1 = seqDbReader.readSeq(idSeq1)
                seq2 = seqDbReader.readSeq(idSeq2)
                if seq1.isNotEmpty() and seq2.isNotEmpty():
                    dotplot = DNADotplot(DotplotData(seq1, seq2))
                    dotplot = dotplot.create()
                    f.write("dotplot created"+"\n")
                    try:
                        store("mydotplot.txt", dotplot)
                    except Exception as e:
                        f.write(str(e))
            except Exception:
                pass
        #read seq 1 and 2 from database
        #make alignment
        #save results to database








