from Models.Database.idbconnection import IDBConnection
from PySide2.QtSql import QSqlQuery
from Models.dotplot import Dotplot
from Models.Database.dotplotTableCreator import *


class DotplotDBWriter:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def write(self, dotplot: Dotplot):
        sql = f"insert into {DotplotTableCreator.TABLE_NAME}({DotplotTableCreator.SEQ1_COL_NAME}, " \
              f"{DotplotTableCreator.SEQ2_COL_NAME}, " \
              f"{DotplotTableCreator.DOTPLOT_COL_NAME}) values(?, ?, ?)"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, dotplot)
        wasSuccessful = self._conn.executeQuery(query)
        return wasSuccessful

    def __bindQuery(self, query: QSqlQuery, dotplot: Dotplot):
        query.bindValue(0, dotplot.seq1.identifier)
        query.bindValue(1, dotplot.seq2.identifier)
        query.bindValue(2, dotplot.matrixToString())
