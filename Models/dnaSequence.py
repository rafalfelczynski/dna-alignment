from sequence import _Sequence
import copy


class DNASequence(_Sequence):

    def __init__(self, identifier, sequence):
        super().__init__(identifier, sequence)

    def isValid(self):
        sequenceCopy = copy.deepcopy(self.sequence)
        sequenceCopy = sequenceCopy.replace("A", "").replace("C", "").replace("G", "").replace("T", "")
        return sequenceCopy is ""



