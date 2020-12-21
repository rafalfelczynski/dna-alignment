import sys
from Database.dotplotDBWriter import *
from Database.sequencedbreader import *


if __name__ == "__main__":
    if len(sys.argv) > 2:
        idSeq1 = sys.argv[1]
        idSeq2 = sys.argv[2]
        with open("log.txt", "w+", encoding="utf-8") as f:
            f.write(idSeq1+"\n")
            f.write(idSeq2+"\n")
        tab = []
        for i in range(0, 100000):
            tab.append(i/2+3*i/5)
        for i in range(0, 10000):
            sorted(tab)

        #read seq 1 and 2 from database
        #make alignment
        #save results to database








