import sys
import PySide2
from Models.Database.alignmentRepository import *
from Models.Database.alignmentDbProvider import *
from Models.Database.dbconnection import DBConnection
from Models.Database.sequenceRepository import *
from Models.Database.sequenceDbProvider import *
from Models.scoring import Scoring
from Models.sequencesAligner import SequencesAligner

ALIGNMENT_PROGRAM_PATH = "Models/alignmentProgram.py"


def splitArgs(args):
    return ' '.join(args).split("$$$")


if __name__ == "__main__":
    args = splitArgs(sys.argv)
    if len(args) > 2:
        idSeq1 = args[1]
        idSeq2 = args[2]
        try:
            match = float(args[3])
            mismatch = float(args[4])
            gap = float(args[5])
            scoring = Scoring(match, mismatch, gap)
            dbConn = DBConnection()
            seqRepo = SequenceRepository(SequenceDbProvider(dbConn))
            seq1 = seqRepo.readSeq(idSeq1)
            seq2 = seqRepo.readSeq(idSeq2)
            if seq1.isNotEmpty() and seq2.isNotEmpty():
                alignment = SequencesAligner.createAlignment(seq1, seq2, scoring)
                alignDbWriter = AlignmentRepository(AlignmentDbProvider(dbConn))
                alignDbWriter.writeAlignment(alignment)
        except Exception as e:
            with open("log2.txt", "w+", encoding="utf-8") as f:
                [f.write(arg + "\n") for arg in splitArgs(sys.argv)]
                f.write(str(e))









