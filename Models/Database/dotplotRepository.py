from typing import List

from Models.dotplot import Dotplot
from Models.idotplotProvider import IDotplotProvider


class DotplotRepository:

    def __init__(self, provider: IDotplotProvider):
        self._provider = provider

    def deleteDotplot(self, seq1id, seq2id) -> bool:
        return self._provider.delete(seq1id, seq2id)

    def readDotplot(self, seq1Id, seq2Id) -> Dotplot:
        dotplots = self._provider.read(seq1Id, seq2Id)
        if len(dotplots) > 0:
            return dotplots[0]
        return Dotplot(None, None)

    def readAllDotplots(self) -> List[Dotplot]:
        return self._provider.readAll()

    def listAllDotplots(self):
        return self._provider.listAll()

    def writeDotplot(self, dotp):
        return self._provider.write(dotp)

    def checkIfExists(self, seq1Id, seq2Id):
        dotps = self._provider.read(seq1Id, seq2Id)
        return len(dotps) > 0 and dotps[0].isValid()







