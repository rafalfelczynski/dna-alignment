from Models.Database.idbconnection import IDBConnection
from PySide2.QtSql import QSqlQuery
from Models.sequence import Sequence
from Models.scoring import Scoring
from Models.alignment import Alignment
from Models.Database.sequenceDbProvider import SequenceDbProvider
from Models.ialignmentProvider import IAlignmentProvider
from typing import List


class AlignmentDbProvider(IAlignmentProvider):

    TABLE_NAME = "alignments"
    SEQ1_ID_COL_NAME = "seq1_id"
    SEQ2_ID_COL_NAME = "seq2_id"
    SEQ1_ALIGNED_COL_NAME = "seq1_aligned"
    SEQ2_ALIGNED_COL_NAME = "seq2_aligned"
    MATCH_COL_NAME = "match"
    MISMATCH_COL_NAME = "mismatch"
    GAP_COL_NAME = "gap"

    def __init__(self, dbconn: IDBConnection):
        self._conn: IDBConnection = dbconn

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
              f" foreign key({self.SEQ1_ID_COL_NAME}) references {SequenceDbProvider.TABLE_NAME}({SequenceDbProvider.ID_COL_NAME}) on delete cascade," \
              f" foreign key({self.SEQ2_ID_COL_NAME}) references {SequenceDbProvider.TABLE_NAME}({SequenceDbProvider.ID_COL_NAME}) on delete cascade)"
        query = self._conn.createQuery(sql)
        return self._conn.executeQuery(query)

    def write(self, ali: Alignment):
        sql = f"insert into {self.TABLE_NAME}(" \
              f"{self.SEQ1_ID_COL_NAME}," \
              f" {self.SEQ2_ID_COL_NAME}," \
              f" {self.MATCH_COL_NAME}," \
              f" {self.MISMATCH_COL_NAME}," \
              f" {self.GAP_COL_NAME}," \
              f" {self.SEQ1_ALIGNED_COL_NAME}," \
              f" {self.SEQ2_ALIGNED_COL_NAME}) values(?, ?, ?, ?, ?, ?, ?)"
        query = self._conn.createQuery(sql)
        self._bindQuery(query, [ali.seq1.identifier, ali.seq2.identifier, ali.scoring.match,
                                ali.scoring.mismatch, ali.scoring.gap, ali.seq1Aligned, ali.seq2Aligned], 0)
        wasSuccessful = self._conn.executeQuery(query)
        return wasSuccessful

    def read(self, id1, id2, scoring) -> List[Alignment]:
        sql = f"select a.{self.SEQ1_ID_COL_NAME}," \
              f" a.{self.SEQ2_ID_COL_NAME}," \
              f" a.{self.MATCH_COL_NAME}," \
              f" a.{self.MISMATCH_COL_NAME}," \
              f" a.{self.GAP_COL_NAME}," \
              f" a.{self.SEQ1_ALIGNED_COL_NAME}," \
              f" a.{self.SEQ2_ALIGNED_COL_NAME}," \
              f" s.{SequenceDbProvider.SEQ_COL_NAME} as seq1," \
              f" s2.{SequenceDbProvider.SEQ_COL_NAME} as seq2," \
              f" s.{SequenceDbProvider.COMMENT_COL_NAME} as comm1," \
              f" s2.{SequenceDbProvider.COMMENT_COL_NAME} as comm2" \
              f" from {self.TABLE_NAME} a" \
              f" inner join {SequenceDbProvider.TABLE_NAME} s" \
              f" on a.{self.SEQ1_ID_COL_NAME} = s.{SequenceDbProvider.ID_COL_NAME}" \
              f" inner join {SequenceDbProvider.TABLE_NAME} s2" \
              f" on a.{self.SEQ2_ID_COL_NAME} = s2.{SequenceDbProvider.ID_COL_NAME}"
        if bool(id1) and bool(id2) and scoring is not None:
            sql += f' where {self.SEQ1_ID_COL_NAME} = ? and {self.SEQ2_ID_COL_NAME} = ? ' \
                   f'and {self.MATCH_COL_NAME} = ? ' \
                   f'and {self.MISMATCH_COL_NAME} = ? ' \
                   f'and {self.GAP_COL_NAME} = ?'
        query = self._conn.createQuery(sql)
        if bool(id1) and bool(id2) and scoring is not None:
            self._bindQuery(query, [id1, id2, scoring.match, scoring.mismatch, scoring.gap], 0)
        alignments = []
        if self._conn.executeQuery(query):
            while query.next():
                alignmentMap = dict()
                record = query.record()
                for i in range(0, record.count()):
                    field = record.field(i)
                    alignmentMap[field.name()] = field.value()
                alignments.append(self._parseAlignmentMap(alignmentMap))
        return alignments

    def readAll(self):
        return self.read(None, None, None)

    def _parseAlignmentMap(self, align):
        seq1Id = align[self.SEQ1_ID_COL_NAME]
        seq2Id = align[self.SEQ2_ID_COL_NAME]
        seq1 = align["seq1"]
        comm1 = align["comm1"]
        seq2 = align["seq2"]
        comm2 = align["comm2"]
        seq1Aligned = align[self.SEQ1_ALIGNED_COL_NAME]
        seq2Aligned = align[self.SEQ2_ALIGNED_COL_NAME]
        match = float(align[self.MATCH_COL_NAME])
        mismatch = float(align[self.MISMATCH_COL_NAME])
        gap = float(align[self.GAP_COL_NAME])
        alignment = Alignment(Sequence(seq1Id, seq1, comm1), Sequence(seq2Id, seq2, comm2),
                              Scoring(match, mismatch, gap), seq1Aligned, seq2Aligned)
        return alignment

    def delete(self, seq1id, seq2id, scoring) -> bool:
        sql = f"delete from {self.TABLE_NAME}" \
              f" where {self.SEQ1_ID_COL_NAME} = ?" \
              f" and {self.SEQ2_ID_COL_NAME} = ?" \
              f" and {self.MATCH_COL_NAME} = ?" \
              f" and {self.MISMATCH_COL_NAME} = ?" \
              f" and {self.GAP_COL_NAME} = ?"
        query = self._conn.createQuery(sql)
        self._bindQuery(query, [seq1id, seq2id, scoring.match, scoring.mismatch, scoring.gap], 0)
        return self._conn.executeQuery(query)

    def _bindQuery(self, query, values, startInd):
        for i in range(startInd, len(values)+startInd):
            query.bindValue(i, values[i-startInd])







