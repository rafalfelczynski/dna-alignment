import numpy as np
from Models.scoring import Scoring
from Models.sequence import Sequence
from Models.scoringMatrix import ScoringMatrix


class ScoringMatrixCreator:

    def __init__(self, scoring: Scoring):
        self._scoring = scoring
        pass

    def create(self, seq1: Sequence, seq2: Sequence):
        rows, columns = len(seq1.sequence) + 2, len(seq2.sequence) + 2
        matrix = np.zeros(shape=(rows, columns))
        for i in range(0, 2):
            for j in range(0, 2):
                matrix[i, j] = 0
        matrix[2:, 0] = [ord(character) for character in seq1.sequence]
        matrix[0, 2:] = [ord(character) for character in seq2.sequence]
        for c in range(2, columns):
            matrix[1, c] = matrix[1, c - 1] + self._scoring[Scoring.Keys.Gap]
        for r in range(2, rows):
            matrix[r, 1] = matrix[r - 1, 1] + self._scoring[Scoring.Keys.Gap]
        for r in range(2, rows):
            for c in range(2, columns):
                diagonalScore = self._scoring[Scoring.Keys.Match if matrix[0, c] == matrix[r, 0] else Scoring.Keys.Mismatch]
                matrix[r, c] = max(matrix[r - 1, c] + self._scoring[Scoring.Keys.Gap],
                                   matrix[r, c - 1] + self._scoring[Scoring.Keys.Gap],
                                   matrix[r - 1, c - 1] + diagonalScore)
        return ScoringMatrix(matrix, self._scoring)
        pass
