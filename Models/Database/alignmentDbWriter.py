from Models.Database.idbconnection import IDBConnection
from PySide2.QtSql import QSqlQuery
from Models.alignment import Alignment
from Models.Database.alignmentTableCreator import AlignmentTableCreator


class AlignmentDbWriter:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def write(self, alignment: Alignment):
        sql = f"insert into {AlignmentTableCreator.TABLE_NAME}(" \
              f"{AlignmentTableCreator.SEQ1_ID_COL_NAME}," \
              f" {AlignmentTableCreator.SEQ2_COL_NAME}," \
              f" {AlignmentTableCreator.MATCH_COL_NAME}," \
              f" {AlignmentTableCreator.MISMATCH_COL_NAME}," \
              f" {AlignmentTableCreator.GAP_COL_NAME}," \
              f" {AlignmentTableCreator.SEQ1_ALIGNED_COL_NAME}," \
              f" {AlignmentTableCreator.SEQ2_ALIGNED_COL_NAME}) values(?, ?, ?, ?, ?, ?, ?)"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, alignment)
        wasSuccessful = self._conn.executeQuery(query)
        return wasSuccessful

    def __bindQuery(self, query: QSqlQuery, ali: Alignment):
        query.bindValue(0, ali.seq1.identifier)
        query.bindValue(1, ali.seq2.identifier)
        query.bindValue(2, ali.scoring.match)
        query.bindValue(3, ali.scoring.mismatch)
        query.bindValue(4, ali.scoring.gap)
        query.bindValue(5, ali.seq1.sequence)
        query.bindValue(6, ali.seq2.sequence)


