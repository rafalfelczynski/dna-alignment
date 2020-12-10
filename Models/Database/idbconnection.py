from PySide2.QtSql import QSqlDatabase, QSqlQuery


class IDBConnection:

    def connect(self) -> bool:
        pass

    def createQuery(self, sql: str) -> QSqlQuery:
        pass

    def executeQuery(self, query: QSqlQuery) -> bool:
        pass


