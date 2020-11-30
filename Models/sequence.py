

class _Sequence:

    def __init__(self, identifier: str, sequence: str):
        self.identifier: str = identifier
        self.sequence: str = sequence
        pass

    def isValid(self):
        return False

    def canBeMatchedWith(self, seq):
        return type(seq) == type(self)


