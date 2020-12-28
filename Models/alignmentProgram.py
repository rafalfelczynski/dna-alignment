import sys
from Models.Database.seqReader import SeqDBReader
from Models.Database.dbconnection import DBConnection
from Models.alignment import Alignment
from Models.scoring import Scoring
from Models.sequencesAligner import SequencesAligner
from Models.Database.alignmentDbWriter import AlignmentDbWriter


def splitArgs(args):
    return ' '.join(args).split("$$$")


if __name__ == "__main__":
    try:
        with open("log.txt", "w+", encoding="utf-8") as f:
            f.write("przed splitem")
            args = splitArgs(sys.argv)
            f.write("po splicie")
            [f.write(arg + "\n") for arg in splitArgs(sys.argv)]
            if len(args) > 2:
                idSeq1 = args[1]
                idSeq2 = args[2]
                try:
                    match = float(args[3])
                    mismatch = float(args[4])
                    gap = float(args[5])
                    scoring = Scoring(match, mismatch, gap)
                    dbConn = DBConnection()
                    seqDbReader = SeqDBReader(dbConn)
                    seq1 = seqDbReader.readSeq(idSeq1)
                    seq2 = seqDbReader.readSeq(idSeq2)
                    if seq1.isNotEmpty() and seq2.isNotEmpty():
                        alignment = SequencesAligner.createAlignment(seq1, seq2, scoring)
                        alignDbWriter = AlignmentDbWriter(dbConn)
                        alignDbWriter.write(alignment)
                except Exception as e:
                    f.write(str(e))
    except Exception as e:
        with open("log2.txt", "w+", encoding="utf-8") as f:
            [f.write(arg + "\n") for arg in splitArgs(sys.argv)]
            f.write(str(e))









