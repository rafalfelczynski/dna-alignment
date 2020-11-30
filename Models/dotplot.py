from sequence import _Sequence


class DotplotData:

    def __init__(self, seq1: _Sequence, seq2: _Sequence, matrix=None):
        self.seq1 = seq1
        self.seq2 = seq2
        self.dotplot = matrix


class __Dotplot:
    __INVALID_SEQUENCE_ERROR_MSG = "Seq1 or Seq2 is invalid DNASequence"

    def __init__(self, data: DotplotData):
        self._data = data
        self._validator = None

    def data(self):
        return self._data

    def create(self):
        pass



