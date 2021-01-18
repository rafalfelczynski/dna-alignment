

class Scoring:

    def __init__(self, match: float, mismatch: float, gap: float):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

    def isValid(self):
        return self.match is not None and isinstance(self.match, (int, float)) \
               and self.mismatch is not None and isinstance(self.mismatch, (int, float)) \
               and self.gap is not None and isinstance(self.gap, (int, float))


