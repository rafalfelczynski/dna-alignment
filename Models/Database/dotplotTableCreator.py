from idbconnection import *


class DotplotTableCreator:

    TABLE_NAME = "dotplots"
    ID_COL_NAME = "id"
    SEQ1_COL_NAME = "seq1_id"
    SEQ2_COL_NAME = "seq2_id"
    DOTPLOT_COL_NAME = "dotplot"

    def __init__(self, dbconn):
        self.__conn: IDBConnection = dbconn

    def createTable(self):
        sql = f"create table if not exists {self.TABLE_NAME} ({self.ID_COL_NAME} integer identity(1,1), {self.SEQ1_COL_NAME} text, {self.SEQ2_COL_NAME} text, {self.DOTPLOT_COL_NAME} text)"
        query = self.__conn.createQuery(sql)
        return self.__conn.executeQuery(query)
