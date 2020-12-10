from idbconnection import *


class DBException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class DBConnection(IDBConnection):

    __CONNECTION_NAME = "conn1"

    def __init__(self):
        self.__connection: QSqlDatabase = QSqlDatabase.addDatabase("SQLITE3", DBConnection.__CONNECTION_NAME)

    def connect(self) -> bool:
        if not self.__isOpen():
            return self.__connection.open()
        else:
            return True

    def createQuery(self, sql: str) -> QSqlQuery:
        if self.connect():
            query = QSqlQuery(self.__connection)
            query.prepare(sql)
            return query
        else:
            raise DBException("Couldn't connect to database")

    def executeQuery(self, query: QSqlQuery):
        if self.connect():
            succ = query.exec_()
            self.__connection.close()
            return succ
        else:
            raise DBException("Couldn't connect to database")

    def __isOpen(self):
        return self.__connection.isOpen() and self.__connection.isValid()


