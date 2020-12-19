from seqTableCreator import *
from dotplotTableCreator import *
from dbconnection import *


class DatabaseCreator:

    @classmethod
    def createDatabase(cls, conn):
        query = conn.createQuery("PRAGMA journal_mode = WAL")
        conn.executeQuery(query)
        query = conn.createQuery("PRAGMA synchronous = NORMAL")
        conn.executeQuery(query)
        seqTab = SequencesTableCreator(conn)
        dotplotTab = DotplotTableCreator(conn)
        seqTab.createTable()
        dotplotTab.createTable()








