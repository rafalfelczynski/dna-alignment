from Models.sequence import Sequence
import numpy as np
from io import BytesIO
import sys


class Dotplot:
    __INVALID_SEQUENCE_ERROR_MSG = "Seq1 or Seq2 is invalid DNASequence"

    def __init__(self, seq1: Sequence, seq2: Sequence):
        self._seq1: Sequence = seq1
        self._seq2: Sequence = seq2
        self._dotplot: np.ndarray = None

    @property
    def seq1(self):
        return self._seq1

    @property
    def seq2(self):
        return self._seq2

    @property
    def dotplot(self):
        return self._dotplot

    def isValid(self):
        return self._seq1 is not None \
               and self._seq2 is not None \
               and self._dotplot is not None

    def create(self) -> 'Dotplot':
        if self._seq1.isValid() and self._seq2.isValid():
            self._dotplot = self.__matchSequences()
            return self
        else:
            raise ValueError(self.__INVALID_SEQUENCE_ERROR_MSG)

    def setDotplotMatrix(self, matrix: np.ndarray):
        self._dotplot = matrix

    def matrixToString(self) -> str:
        np.set_printoptions(threshold=sys.maxsize)
        buffer = BytesIO()
        np.savetxt(buffer, self._dotplot, fmt="%d", encoding="utf-8", delimiter="")
        return buffer.getvalue().decode("utf-8")

    def matrixFromString(self, string: str, rows, columns):
        string = string.replace("\n", "")
        if len(string) != rows*columns:
            print("len", len(string), rows*columns, rows, columns)
            raise ValueError("Rows, columns and string length don't match!")
        matrix = np.zeros(shape=(rows, columns), dtype=int)
        for i in range(0, rows):
            for j in range(0, columns):
                matrix[i, j] = int(string[i*columns+j])
        self._dotplot = matrix

    def mapToXY(self):
        rows, cols = self.dotplot.nonzero()
        return cols.tolist(), rows.tolist()

    def __matchSequences(self):
        seq1String: str = self._seq1.sequence
        seq2String: str = self._seq2.sequence
        rows = len(seq1String)
        columns = len(seq2String)
        matrix = np.empty(shape=(rows, columns), dtype=int)
        for i in range(0, rows):
            for j in range(0, columns):
                matrix[i, j] = 1 if seq1String[i] == seq2String[j] else 0
        return matrix



