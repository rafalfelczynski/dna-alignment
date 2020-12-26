import copy


class NotValidSequenceException(Exception):
    def __init__(self, msg="File does not valid sequence"):
        super().__init__(msg)


class Sequence:

    def __init__(self, identifier: str, sequence: str):
        self.identifier: str = identifier
        self.sequence: str = sequence

    def isNotEmpty(self):
        return self.identifier and self.sequence

    def isValid(self):
        sequenceCopy = copy.deepcopy(self.sequence)
        sequenceCopy = sequenceCopy.replace("A", "").replace("C", "").replace("G", "").replace("T", "")
        return sequenceCopy == "" and self.isNotEmpty()

    def cutSequenceIntoFragments(self, fragmLength):
        cutSequence = ""
        for i in range(0, len(self.sequence), fragmLength):
            cutSequence += f"{self.sequence[i:i+fragmLength]}\n"
        return cutSequence
