import math

import numpy as np

from Models.scoring import Scoring


def _isclose(a, b):
    return math.isclose(a, b, rel_tol=0.0001, abs_tol=0.00001)


class PathFinder:

    @staticmethod
    def getAlignedSequences(matrix: np.ndarray, scoring: Scoring) -> (str, str):
        r, c = matrix.shape
        r -= 1
        c -= 1
        seq1: str = ""
        seq2: str = ""
        while r > 1 or c > 1:
            points = scoring.match if _isclose(matrix[r, 0], matrix[0, c]) else scoring.mismatch
            if c > 1 and r > 1 and _isclose(matrix[r, c], matrix[r-1, c-1] + points):
                seq1 = chr(int(matrix[r, 0])) + seq1
                seq2 = chr(int(matrix[0, c])) + seq2
                r -= 1
                c -= 1
            elif c > 1 and _isclose(matrix[r, c], matrix[r, c-1] + scoring.gap):
                seq1 = '-' + seq1
                seq2 = chr(int(matrix[0, c])) + seq2
                c -= 1
            else:
                seq1 = chr(int(matrix[r, 0])) + seq1
                seq2 = '-' + seq2
                r -= 1
        return seq1, seq2




