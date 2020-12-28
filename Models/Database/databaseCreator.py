from Models.Database.seqTableCreator import SequencesTableCreator
from Models.Database.dotplotTableCreator import DotplotTableCreator
from Models.Database.dbconnection import IDBConnection
from Models.Database.alignmentTableCreator import AlignmentTableCreator


class DatabaseCreator:

    @classmethod
    def createDatabase(cls, conn: IDBConnection):
        query = conn.createQuery("PRAGMA journal_mode = WAL;")
        conn.executeQuery(query)
        query = conn.createQuery("PRAGMA synchronous = NORMAL;")
        conn.executeQuery(query)
        query = conn.createQuery("PRAGMA foreign_keys = ON;")
        conn.executeQuery(query)
        seqTab = SequencesTableCreator(conn)
        seqTab.createTable()
        dotplotTab = DotplotTableCreator(conn)
        dotplotTab.createTable()
        alignmentTab = AlignmentTableCreator(conn)
        alignmentTab.createTable()








