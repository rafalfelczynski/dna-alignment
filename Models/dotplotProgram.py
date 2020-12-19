import sys
from dotplotDBWriter import *
from sequencedbreader import *
from dbconnection import *



if __name__ == "__main__":
    if len(sys.argv) == 2:
        idSeq1 = sys.argv[1]
        idSeq2 = sys.argv[2]
        dbConnection = DBConnection()
        seqReader = SequenceDBReader(dbConnection)
        seqsFromDb = seqReader.read(["*"], SequencesTableCreator.ID_COL_NAME + f" in ({idSeq1}, {idSeq2})")
        if len(seqsFromDb) == 2:
            if seqsFromDb[0].identifier == idSeq1:
                seq1 = seqsFromDb[0]
                seq2 = seqsFromDb[1]
            else:
                seq1 = seqsFromDb[1]
                seq2 = seqsFromDb[0]
            dotplot = DNADotplot(DotplotData(seq1, seq2))
            dotplot.create()
            writer = DotplotDBWriter(dbConnection)
            writer.write(dotplot)
        #read seq 1 and 2 from database
        #make dotplot
        #save results to database








