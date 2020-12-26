from Models.isequpdater import ISeqUpdater
from Models.Database.sequencedbupdater import SequenceDbUpdater


class SeqDbUpdater(ISeqUpdater):

    def __init__(self, dbConn):
        self._conn = dbConn
        self._updater = SequenceDbUpdater(self._conn)

    def deleteSeq(self, id: str) -> bool:
        return self._updater.delete(id)




