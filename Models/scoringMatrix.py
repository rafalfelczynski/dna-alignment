import numpy as np
from Models.scoring import Scoring
from collections import deque
from typing import Deque
import math


def _isclose(a, b):
    return math.isclose(a, b, rel_tol=0.0001, abs_tol=0.00001)


class ScoringMatrix:

    def __init__(self, matrix: np.ndarray, scoring: Scoring):
        self._matrix: np.ndarray = matrix
        self._scoring: Scoring = scoring
        pass

    def fetchAligned(self):
        r, c = self._matrix.shape
        r -= 1
        c -= 1
        seq1: Deque[chr] = deque()
        seq2: Deque[chr] = deque()
        match, mismatch, gap = self.__fetchScores()
        while r > 1 or c > 1:
            points = match if _isclose(self._matrix[r, 0], self._matrix[0, c]) else mismatch
            if c > 1 and r > 1 and _isclose(self._matrix[r, c], self._matrix[r-1, c-1] + points):
                seq1.appendleft(chr(int(self._matrix[r, 0])))
                seq2.appendleft(chr(int(self._matrix[0, c])))
                r -= 1
                c -= 1
            elif c > 1 and _isclose(self._matrix[r, c], self._matrix[r, c-1] + gap):
                seq1.appendleft('-')
                seq2.appendleft(chr(int(self._matrix[0, c])))
                c -= 1
            else:
                seq1.appendleft(chr(int(self._matrix[r, 0])))
                seq2.appendleft('-')
                r -= 1
        return "".join(seq1), "".join(seq2)

    def __fetchScores(self):
        try:
            match = self._scoring[Scoring.Keys.Match]
            mismatch = self._scoring[Scoring.Keys.Match]
            gap = self._scoring[Scoring.Keys.Gap]
            return match, mismatch, gap
        except ValueError as er:
            print(er)  # Print to log file!
            exit(-1)

    def __repr__(self):
        return self._matrix.__repr__()




