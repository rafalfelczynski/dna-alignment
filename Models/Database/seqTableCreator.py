from Models.Database.idbconnection import *


class SequencesTableCreator:

    TABLE_NAME = "sequences"
    ID_COL_NAME = "id"
    SEQ_COL_NAME = "sequence"

    def __init__(self, dbconn):
        self.__conn: IDBConnection = dbconn

    def createTable(self):
        sql = f"create table if not exists {self.TABLE_NAME}(" \
              f"{self.ID_COL_NAME} text primary key," \
              f" {self.SEQ_COL_NAME} text not null)"
        query = self.__conn.createQuery(sql)
        return self.__conn.executeQuery(query)





