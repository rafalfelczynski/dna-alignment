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

    def ids(self) -> (str, str, str, str, str):
        return self._seq1.identifier, self._seq2.identifier, str(self._scoring.match), str(self.scoring.mismatch), str(
            self.scoring.gap)

    def isValid(self):
        return self._seq1 is not None \
               and self._seq2 is not None \
               and self._scoring is not None \
               and bool(self._seq1Aligned) \
               and len(self._seq1Aligned) == len(self._seq2Aligned)

    def matchLines(self):
        return "".join(["|" if self._seq1Aligned[i] == self._seq2Aligned[i] else " "
                        for i in range(0, min(len(self._seq1Aligned), len(self._seq2Aligned)))])

    def info(self) -> str:
        info = ""
        info += f"Sequence 1:\n{self.seq1.identifier} {self.seq1.comment}\n"
        info += f"Sequence 2:\n{self.seq2.identifier} {self.seq2.comment}\n"
        info += self.statistics()
        info += "Aligned sequences:\n"
        info += self.cutInFragments(50)
        return info

    def statistics(self) -> str:
        stat = f"Match: {self.scoring.match}\n"
        stat += f"Mismatch: {self.scoring.mismatch}\n"
        stat += f"Gap: {self.scoring.gap}\n"
        nOfGaps = self._getNumberOfGaps(self.seq1Aligned, self.seq1.sequence)
        stat += f"Number of gaps in Sequence 1: {nOfGaps}\n"
        stat += f"Gaps as percent of initial Sequence 1:{nOfGaps/len(self.seq1.sequence)*100 : 3.1f}%\n"
        nOfGaps = self._getNumberOfGaps(self.seq2Aligned, self.seq2.sequence)
        stat += f"Number of gaps in Sequence 2: {nOfGaps}\n"
        stat += f"Gaps as percent of initial Sequence 2:{nOfGaps/len(self.seq2.sequence)*100 : 3.1f}%\n"
        return stat

    def _getNumberOfGaps(self, string, refString):
        return len(string) - len(refString)

    def cutInFragments(self, fragmLength):
        cutSequence = ""
        matchLines = self.matchLines()
        for i in range(0, len(self._seq1Aligned), fragmLength):
            idMaxLen = 20
            cutSequence += f">{self._seq1.identifier:{idMaxLen}}\t{self._seq1Aligned[i: i + fragmLength]}\t{min(i + fragmLength, len(self._seq1Aligned))}\n"
            cutSequence += f"{'':{idMaxLen}}\t{matchLines[i: i + fragmLength]}\n"
            cutSequence += f">{self._seq2.identifier:{idMaxLen}}\t{self._seq2Aligned[i: i + fragmLength]}\t{min(i + fragmLength, len(self._seq2Aligned))}\n"
            cutSequence += "\n"
        return cutSequence
