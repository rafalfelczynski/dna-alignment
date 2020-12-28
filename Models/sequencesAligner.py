import numpy as np
from Models.PathFinder import PathFinder
from Models.sequence import Sequence
from Models.scoring import Scoring
from Models.alignment import Alignment


class SequencesAligner:

    @staticmethod
    def createAlignment(seq1: Sequence, seq2: Sequence, scoring: Scoring) -> Alignment:
        matrix = SequencesAligner._createScoringMatrix(seq1, seq2, scoring)
        seq1Aligned, seq2Aligned = PathFinder.getAlignedSequences(matrix, scoring)
        return Alignment(seq1, seq2, scoring, seq1Aligned, seq2Aligned)

    @staticmethod
    def _createScoringMatrix(seq1: Sequence, seq2: Sequence, scoring: Scoring):
        rows, columns = len(seq1.sequence) + 2, len(seq2.sequence) + 2
        matrix = np.zeros(shape=(rows, columns))
        for i in range(0, 2):
            for j in range(0, 2):
                matrix[i, j] = 0
        matrix[2:, 0] = [ord(character) for character in seq1.sequence]
        matrix[0, 2:] = [ord(character) for character in seq2.sequence]
        for c in range(2, columns):
            matrix[1, c] = matrix[1, c - 1] + scoring.gap
        for r in range(2, rows):
            matrix[r, 1] = matrix[r - 1, 1] + scoring.gap
        for r in range(2, rows):
            for c in range(2, columns):
                diagonalScore = scoring.match if matrix[0, c] == matrix[r, 0] else scoring.mismatch
                matrix[r, c] = max(matrix[r - 1, c] + scoring.gap,
                                   matrix[r, c - 1] + scoring.gap,
                                   matrix[r - 1, c - 1] + diagonalScore)
        return matrix




