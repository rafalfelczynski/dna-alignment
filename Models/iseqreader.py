from Models.sequence import Sequence
from typing import List


class ISeqReader:

    def readSeq(self, id: str) -> Sequence:
        pass

    def readAll(self) -> List[Sequence]:
        pass

    def checkIfExists(self, id: str) -> bool:
        pass






