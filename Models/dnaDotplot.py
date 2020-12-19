from dotplot import Dotplot
import numpy as np
from dotplot import DotplotData


class DNADotplot(Dotplot):

    __INVALID_SEQUENCE_ERROR_MSG = "Seq1 or Seq2 is invalid DNASequence"

    def __init__(self, data: DotplotData):
        super().__init__(data)

    def create(self):
        if self._data.seq1.isValid() \
                and self._data.seq2.isValid() \
                and self._data.seq1.canBeMatchedWith(self._data.seq2):
            self._data.dotplot = self.__matchSequences()
            return self._data.dotplot
        else:
            raise ValueError(self.__INVALID_SEQUENCE_ERROR_MSG)

    def __matchSequences(self):
        seq1String: str = self._data.seq1.sequence
        seq2String: str = self._data.seq2.sequence
        rows = len(seq1String) + 1
        columns = len(seq2String) + 1
        matrix = np.empty(shape=(rows, columns), dtype=str)
        matrix[0, 0] = " "
        matrix[1::, 0] = list(seq1String)
        matrix[0, 1::] = list(seq2String)
        for i in range(1, rows):
            for j in range(1, columns):
                matrix[i, j] = "." if matrix[i, 0] == matrix[0, j] else " "
        return matrix

