from typing import List
from Models.dotplot import Dotplot


class IDotplotProvider:

    def read(self, id1, id2) -> List[Dotplot]:
        pass

    def listAll(self) -> List[Dotplot]:
        """Gets invalid doptlots to lists only identifiers of all dotplots, dot reading matrixes from database"""
        pass

    def readAll(self) -> List[Dotplot]:
        pass

    def write(self, dotp) -> bool:
        pass

    def delete(self, id1, id2):
        pass







