from Models.Database.idbconnection import *
from Models.Database.seqTableCreator import SequencesTableCreator


class AlignmentTableCreator:

    TABLE_NAME = "alignments"
    SEQ1_ID_COL_NAME = "seq1_id"
    SEQ2_ID_COL_NAME = "seq2_id"
    SEQ1_ALIGNED_COL_NAME = "seq1_aligned"
    SEQ2_ALIGNED_COL_NAME = "seq2_aligned"
    MATCH_COL_NAME = "match"
    MISMATCH_COL_NAME = "mismatch"
    GAP_COL_NAME = "gap"

    def __init__(self, dbconn):
        self.__conn: IDBConnection = dbconn

    def createTable(self):
        sql = f"create table if not exists {self.TABLE_NAME} (" \
              f" {self.SEQ1_ID_COL_NAME} text not null," \
              f" {self.SEQ2_ID_COL_NAME} text not null," \
              f" {self.MATCH_COL_NAME} real not null, " \
              f" {self.MISMATCH_COL_NAME} real not null, " \
              f" {self.GAP_COL_NAME} real not null," \
              f" {self.SEQ1_ALIGNED_COL_NAME} text not null," \
              f" {self.SEQ2_ALIGNED_COL_NAME} text not null," \
              f" primary key({self.SEQ1_ID_COL_NAME}, {self.SEQ2_ID_COL_NAME}, {self.MATCH_COL_NAME}, {self.MISMATCH_COL_NAME}, {self.GAP_COL_NAME})," \
              f" foreign key({self.SEQ1_ID_COL_NAME}) references {SequencesTableCreator.TABLE_NAME}({SequencesTableCreator.ID_COL_NAME}) on delete cascade," \
              f" foreign key({self.SEQ2_ID_COL_NAME}) references {SequencesTableCreator.TABLE_NAME}({SequencesTableCreator.ID_COL_NAME}) on delete cascade)"
        query = self.__conn.createQuery(sql)
        return self.__conn.executeQuery(query)