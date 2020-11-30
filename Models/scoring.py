from enum import Enum


class Scoring:
    class Keys(Enum):
        Match = "match"
        Mismatch = "mismatch"
        Gap = "gap"
    pass

    @staticmethod
    def isAllowedKey(key):
        return key in set(key.value for key in Scoring.Keys)

    @staticmethod
    def toKey(key: str):
        return Scoring.Keys(key)

    def __init__(self):
        self._scoring = dict()

    def __setitem__(self, key: 'Scoring.Keys', value: float):
        if key in self.Keys:
            self._scoring[key] = value

    def __getitem__(self, key: 'Scoring.Keys'):
        return self._scoring[key]


