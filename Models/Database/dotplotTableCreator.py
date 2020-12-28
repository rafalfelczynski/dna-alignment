from Models.Database.idbconnection import *
from Models.Database.seqTableCreator import SequencesTableCreator


class DotplotTableCreator:

    TABLE_NAME = "dotplots"
    SEQ1_COL_NAME = "seq1_id"
    SEQ2_COL_NAME = "seq2_id"
    DOTPLOT_COL_NAME = "dotplot"

    def __init__(self, dbconn):
        self.__conn: IDBConnection = dbconn

    def createTable(self):
        sql = f"create table if not exists {self.TABLE_NAME} (" \
              f" {self.SEQ1_COL_NAME} text not null," \
              f" {self.SEQ2_COL_NAME} text not null," \
              f" {self.DOTPLOT_COL_NAME} text not null," \
              f" primary key({self.SEQ1_COL_NAME}, {self.SEQ2_COL_NAME})," \
              f" foreign key({self.SEQ1_COL_NAME}) references {SequencesTableCreator.TABLE_NAME}({SequencesTableCreator.ID_COL_NAME}) on delete cascade," \
              f" foreign key({self.SEQ2_COL_NAME}) references {SequencesTableCreator.TABLE_NAME}({SequencesTableCreator.ID_COL_NAME}) on delete cascade)"
        query = self.__conn.createQuery(sql)
        return self.__conn.executeQuery(query)
