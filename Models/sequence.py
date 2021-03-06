

class NotValidSequenceException(Exception):
    def __init__(self, msg="File does not valid sequence"):
        super().__init__(msg)


class Sequence:

    def __init__(self, identifier: str, sequence: str, comment: str=None):
        self.identifier: str = identifier
        self.sequence: str = sequence
        self.comment: str = comment

    def isNotEmpty(self) -> bool:
        return bool(self.identifier) and bool(self.sequence)

    def isValid(self):
        def countCharacters(ch):
            nonlocal A, T, C, G
            if ch == 'A':
                A += 1
            elif ch == 'T':
                T += 1
            elif ch == 'C':
                C += 1
            elif ch == 'G':
                G += 1
        A, T, C, G = 0, 0, 0, 0
        [countCharacters(ch) for ch in self.sequence]
        return self.isNotEmpty() and A+T+C+G == len(self.sequence)

    def cutSequenceIntoFragments(self, fragmLength):
        cutSequence = ""
        for i in range(0, len(self.sequence), fragmLength):
            cutSequence += f"{self.sequence[i:i+fragmLength]}\n"
        return cutSequence
