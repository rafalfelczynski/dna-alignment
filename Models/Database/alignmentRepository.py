from Models.alignment import Alignment
from Models.sequence import Sequence
from Models.scoring import Scoring
from typing import List
from Models.ialignmentProvider import IAlignmentProvider


class AlignmentRepository:

    def __init__(self, provider: IAlignmentProvider):
        self._provider = provider

    def readAlignment(self, seq1Id, seq2Id, scoring: Scoring) -> Alignment:
        alignments = self._provider.read(seq1Id, seq2Id, scoring)
        if len(alignments) > 0:
            return alignments[0]
        return Alignment()

    def readAllAlignments(self) -> List[Alignment]:
        return self._provider.readAll()

    def checkIfExists(self, seq1Id, seq2Id, scoring: Scoring):
        return self.readAlignment(seq1Id, seq2Id, scoring).isValid()

    def writeAlignment(self, alignment) -> bool:
        return self._provider.write(alignment)

    def deleteAlignment(self, seq1id, seq2id, scoring: Scoring) -> bool:
        return self._provider.delete(seq1id, seq2id, scoring)









