from Models.Database.sequenceDbProvider import SequenceDbProvider
from Models.Database.dotplotDbProvider import DotplotDbProvider
from Models.Database.dbconnection import IDBConnection
from Models.Database.alignmentDbProvider import AlignmentDbProvider


class DatabaseCreator:

    @classmethod
    def createDatabase(cls, conn: IDBConnection):
        query = conn.createQuery("PRAGMA journal_mode = WAL;")
        conn.executeQuery(query)
        query = conn.createQuery("PRAGMA synchronous = NORMAL;")
        conn.executeQuery(query)
        query = conn.createQuery("PRAGMA foreign_keys = ON;")
        conn.executeQuery(query)
        seqTab = SequenceDbProvider(conn)
        seqTab.createTable()
        dotplotTab = DotplotDbProvider(conn)
        dotplotTab.createTable()
        alignmentTab = AlignmentDbProvider(conn)
        alignmentTab.createTable()








