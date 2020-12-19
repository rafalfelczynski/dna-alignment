import sys
from dotplotDBWriter import *
from sequencedbreader import *



if __name__ == "__main__":
    if len(sys.argv) == 2:
        idSeq1 = sys.argv[1]
        idSeq2 = sys.argv[2]
        seqReader = SequenceDBReader()
        #read seq 1 and 2 from database
        #make alignment
        #save results to database








