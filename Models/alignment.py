from Models.sequence import Sequence
from Models.scoring import Scoring


class Alignment:

    def __init__(self, seq1: Sequence = None, seq2: Sequence = None, scoring: Scoring = None,
                 seq1Aligned: str = None, seq2Aligned: str = None):
        self._seq1 = seq1
        self._seq2 = seq2
        self._scoring = scoring
        self._seq1Aligned = seq1Aligned
        self._seq2Aligned = seq2Aligned

    @property
    def seq1(self):
        return self._seq1

    @property
    def seq2(self):
        return self._seq2

    @property
    def scoring(self):
        return self._scoring

    @property
    def seq1Aligned(self):
        return self._seq1Aligned

    @property
    def seq2Aligned(self):
        return self._seq2Aligned

    def isValid(self):
        return self._seq1 is not None \
               and self._seq2 is not None \
               and self._scoring is not None \
               and bool(self._seq1Aligned) \
               and bool(self._seq2Aligned)
