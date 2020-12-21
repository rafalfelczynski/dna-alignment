from Models.sequence import Sequence
import copy


class DNASequence(Sequence):

    def __init__(self, identifier, sequence):
        super().__init__(identifier, sequence)

    def isValid(self):
        sequenceCopy = copy.deepcopy(self.sequence)
        sequenceCopy = sequenceCopy.replace("A", "").replace("C", "").replace("G", "").replace("T", "")
        return sequenceCopy == ""



