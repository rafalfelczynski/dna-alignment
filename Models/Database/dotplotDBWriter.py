from idbconnection import *
from dotplot import *
from dotplotTableCreator import *


class DotplotDBWriter:

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

    def write(self, dotplot: Dotplot):
        sql = f"insert into {DotplotTableCreator.TABLE_NAME}({DotplotTableCreator.SEQ1_COL_NAME}, " \
                                                            f"{DotplotTableCreator.SEQ2_COL_NAME}, " \
                                                            f"{DotplotTableCreator.DOTPLOT_COL_NAME}) values(?, ?, ?)"
        query = self._conn.createQuery(sql)
        self.__bindQuery(query, dotplot.data())
        return self._conn.executeQuery(query)


    def __bindQuery(self, query: QSqlQuery, dotplot: DotplotData):
        query.bindValue(0, dotplot.seq1)
        query.bindValue(1, dotplot.seq2)
        query.bindValue(2, dotplot.dotplot)







