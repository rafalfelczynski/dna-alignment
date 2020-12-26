from Models.Database.idbconnection import *


class DBException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class DBConnection(IDBConnection):

    __index = 0
    DB_NAME = "alignment_app.db"

    def __init__(self):
        self.__connectionName = "conn"+str(DBConnection.__index)
        DBConnection.__index += 1
        self.__connection: QSqlDatabase = QSqlDatabase.addDatabase("QSQLITE", self.__connectionName)
        self.__connection.setDatabaseName(self.DB_NAME)

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
            raise DBException("Couldn't connect to database "+ self.__connection.lastError().text())

    def executeQuery(self, query: QSqlQuery):
        if self.connect():
            succ = query.exec_()
            return succ
        else:
            raise DBException("Couldn't connect to database")

    def lastError(self):
        return self.__connection.lastError()

    def close(self):
        self.__connection.close()

    def __isOpen(self):
        return self.__connection.isOpen() and self.__connection.isValid()



