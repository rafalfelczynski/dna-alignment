from typing import List
from Models.sequence import Sequence
from Models.isequenceProvider import ISequenceProvider


class SequenceRepository:

    def __init__(self, provider: ISequenceProvider):
        self._provier = provider

    def writeSeq(self, seq: Sequence) -> bool:
        return self._provier.write(seq)

    def readSeq(self, id) -> Sequence:
        readSeqs = self._provier.read(id)
        if len(readSeqs) > 0:
            return readSeqs[0]
        return Sequence("", "")

    def readAll(self) -> List[Sequence]:
        return self._provier.readAll()

    def checkIfExists(self, id):
        return self._provier.checkIfExists(id)

    def deleteSeq(self, id: str) -> bool:
        return self._provier.delete(id)







