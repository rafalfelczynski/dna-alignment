import sys
from io import BytesIO

import numpy as np

from Models.dotplot import Dotplot
from Models.sequence import Sequence


def dotplotMatrixToString(dotplot: Dotplot):
    buffer = BytesIO()
    np.savetxt(buffer, dotplot.dotplot, fmt="%d", encoding="utf-8", delimiter="")
    return buffer.getvalue().decode("utf-8")


def matrixToStr(matrix: np.ndarray):
    string = ""
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            string += matrix[i, j]
        string += "\n"
    return string


def storeMatrix(filePath: str, dotplot: Dotplot):
    with open(filePath, "w", encoding="utf-8") as dotplotFile:
        dotplotFile.write(dotplot.seq1.identifier+"\n")
        dotplotFile.write(dotplot.seq1.sequence+"\n")
        dotplotFile.write(dotplot.seq2.identifier+"\n")
        dotplotFile.write(dotplot.seq2.sequence+"\n")
        np.set_printoptions(threshold=sys.maxsize)
        buffer = BytesIO()
        np.savetxt(buffer, dotplot.dotplot, fmt="%d", encoding="utf-8", delimiter="")
        dotplotFile.write(buffer.getvalue().decode("utf-8"))


def storeIndexes(filePath: str, dotplot: Dotplot):
    with open(filePath, "w", encoding="utf-8") as dotplotFile:
        dotplotFile.write(dotplot.seq1.identifier+"\n")
        dotplotFile.write(dotplot.seq1.sequence+"\n")
        dotplotFile.write(dotplot.seq2.identifier+"\n")
        dotplotFile.write(dotplot.seq2.sequence+"\n")
        np.set_printoptions(threshold=sys.maxsize)
        np.savetxt(dotplotFile, np.where(dotplot.dotplot.flatten() == 1), fmt="%d", encoding="utf-8", delimiter=" ")


def loadMatrix(filePath: str):
    with open(filePath, "r") as dotplotFile:
        seq1id = dotplotFile.readline()[0:-1]  # [0:-1] because there is \n at the end of the line
        seq1sequence = dotplotFile.readline()[0:-1]
        seq2id = dotplotFile.readline()[0:-1]
        seq2sequence = dotplotFile.readline()[0:-1]
        rows = len(seq1sequence)
        columns = len(seq2sequence)
        matrix = np.zeros(shape=(rows, columns))
        for i in range(0, rows):
            line = dotplotFile.readline()
            for j in range(0, columns):
                matrix[i, j] = line[j]
        return Dotplot(Sequence(seq1id, seq1sequence), Sequence(seq2id, seq2sequence), matrix)


def loadIndexes(filePath: str):
    with open(filePath, "r") as dotplotFile:
        seq1id = dotplotFile.readline()[0:-1]  # [0:-1] because there is \n at the end of the line
        seq1sequence = dotplotFile.readline()[0:-1]
        seq2id = dotplotFile.readline()[0:-1]
        seq2sequence = dotplotFile.readline()[0:-1]
        rows = len(seq1sequence)
        columns = len(seq2sequence)
        matrix = np.zeros(shape=(rows, columns))
        lines = dotplotFile.readlines()
        for line in lines:
            indexes = line.split(" ")
            for i in indexes:
                i = int(i)
                row = i//columns
                matrix[row, i-row*columns] = 1
        return Dotplot(Sequence(seq1id, seq1sequence), Sequence(seq2id, seq2sequence), matrix)


