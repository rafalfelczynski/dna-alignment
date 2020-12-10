from idbcreator import *
from idbconnection import *


class SequencesTableCreator(IDBCreator):

    class __SequenceDbInfo:
        TABLE_NAME = "sequences"

    @classmethod
    def TABLE_NAME(cls):
        return str(cls.__SequenceDbInfo.TABLE_NAME)

    def __init__(self, dbconn):
        self.__conn: IDBConnection = dbconn

    def tableName(self):
        return SequencesTableCreator.TABLE_NAME()

    def createTable(self):
        sql = f"create table if not exists {self.tableName()}(id text, sequence text)"
        query = self.__conn.createQuery(sql)
        return self.__conn.executeQuery(query)





