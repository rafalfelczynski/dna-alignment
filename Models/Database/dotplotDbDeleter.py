from Models.idotplotDeleter import IDotplotDeleter
from Models.Database.dotplotDbDeleterWorker import DotplotDbDeleterWorker


class DotplotDbDeleter(IDotplotDeleter):

    def __init__(self, dbConn):
        self._deleter = DotplotDbDeleterWorker(dbConn)

    def deleteDotplot(self, seq1id, seq2id) -> bool:
        return self._deleter.delete(seq1id, seq2id)



