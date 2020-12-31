from PySide2.QtSql import QSqlQuery


class IDBConnection:

    def connect(self) -> bool:
        pass

    def createQuery(self, sql: str) -> QSqlQuery:
        pass

    def executeQuery(self, query: QSqlQuery) -> bool:
        pass

    def lastError(self) -> str:
        pass

    def close(self) -> None:
        pass


