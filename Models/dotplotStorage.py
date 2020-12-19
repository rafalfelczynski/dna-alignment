import numpy as np
from dnaDotplot import DNADotplot
from dnaSequence import DNASequence
from dotplot import Dotplot, DotplotData
from PySide2.QtCore import QRegExp


def store(filePath: str, dotplot: DotplotData):
    with open(filePath, "w") as dotplotFile:
        dotplotFile.write(dotplot.seq1.identifier+"\n")
        dotplotFile.write(dotplot.seq1.sequence+"\n")
        dotplotFile.write(dotplot.seq2.identifier+"\n")
        dotplotFile.write(dotplot.seq2.sequence+"\n")
        dotplotFile.write(str(dotplot.dotplot))
        #np.savetxt(dotplotFile, dotplot.dotplot, fmt="%c", encoding="utf-8", delimiter="")
    pass


def __load(filePath: str):
    with open(filePath, "r") as dotplotFile:
        seq1id = dotplotFile.readline()[0:-1]  # [0:-1] because there is \n at the end of the line
        seq1sequence = dotplotFile.readline()[0:-1]
        seq2id = dotplotFile.readline()[0:-1]
        seq2sequence = dotplotFile.readline()[0:-1]
        rows = len(seq1sequence)+1
        columns = len(seq2sequence)+1
        matrix = np.empty(shape=(rows, columns), dtype=str)
        regex = QRegExp("('.')")
        for i in range(0, rows):
            line = dotplotFile.readline()[0:-1].replace("[", "").replace("]", "")
            pos: int = 0
            chars = []
            while pos >= 0:
                pos = regex.indexIn(line, pos)
                if pos >= 0:
                    chars.append(regex.cap(1))
                    pos += regex.matchedLength()
            matrix[i] = chars
        return seq1id, seq1sequence, seq2id, seq2sequence, matrix


def loadDNA(filePath: str):
    seq1id, seq1sequence, seq2id, seq2sequence, matrix = __load(filePath)
    dotplot = DNADotplot(DotplotData(DNASequence(seq1id, seq1sequence), DNASequence(seq2id, seq2sequence), matrix))
    return dotplot


