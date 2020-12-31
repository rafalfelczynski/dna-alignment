from Models.ialignmentDeleter import IAlignmentDeleter
from Models.Database.alignmentDbDeleterWorker import AlignmentDbDeleterWorker
from Models.scoring import Scoring


class AlignmentDbDeleter(IAlignmentDeleter):

    def __init__(self, dbconn):
        self._deleter = AlignmentDbDeleterWorker(dbconn)

    def deleteAlignment(self, seq1id, seq2id, scoring: Scoring) -> bool:
        return self._deleter.delete(seq1id, seq2id, scoring.match, scoring.mismatch, scoring.gap)




