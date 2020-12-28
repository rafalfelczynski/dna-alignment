from Models.Database.idbconnection import IDBConnection
from Models.Database.seqTableCreator import SequencesTableCreator
from Models.Database.alignmentTableCreator import AlignmentTableCreator
from typing import List, Dict
from Models.alignment import Alignment
from Models.sequence import Sequence
from Models.scoring import Scoring


class AlignmentDbReader:

    def __init__(self, dbConn: IDBConnection):
        self._conn = dbConn

    def read(self, where=None, whereValues=None) -> List[Alignment]:
        sql = f"select a.{AlignmentTableCreator.SEQ1_ID_COL_NAME}," \
              f" a.{AlignmentTableCreator.SEQ2_COL_NAME}," \
              f" a.{AlignmentTableCreator.MATCH_COL_NAME}," \
              f" a.{AlignmentTableCreator.MISMATCH_COL_NAME}," \
              f" a.{AlignmentTableCreator.GAP_COL_NAME}," \
              f" a.{AlignmentTableCreator.SEQ1_ALIGNED_COL_NAME}," \
              f" a.{AlignmentTableCreator.SEQ2_ALIGNED_COL_NAME}," \
              f" s.{SequencesTableCreator.SEQ_COL_NAME} as seq1," \
              f" s2.{SequencesTableCreator.SEQ_COL_NAME} as seq2" \
              f" from {AlignmentTableCreator.TABLE_NAME} a" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s" \
              f" on a.{AlignmentTableCreator.SEQ1_ID_COL_NAME} = s.{SequencesTableCreator.ID_COL_NAME}" \
              f" inner join {SequencesTableCreator.TABLE_NAME} s2" \
              f" on a.{AlignmentTableCreator.SEQ1_ID_COL_NAME} = s2.{SequencesTableCreator.ID_COL_NAME}"
        if where is not None and where != "":
            sql += f" where {where}"
        query = self._conn.createQuery(sql)
        if where is not None and where != "":
            self.__bindQuery(query, whereValues)
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

    def __bindQuery(self, query, whereValues):
        for i in range(0, len(whereValues)):
            query.bindValue(i, whereValues[i])

    def _parseAlignmentMap(self, align):
        seq1Id = align[AlignmentTableCreator.SEQ1_ID_COL_NAME]
        seq2Id = align[AlignmentTableCreator.SEQ2_COL_NAME]
        seq1 = align["seq1"]
        seq2 = align["seq2"]
        seq1Aligned = align[AlignmentTableCreator.SEQ1_ALIGNED_COL_NAME]
        seq2Aligned = align[AlignmentTableCreator.SEQ2_ALIGNED_COL_NAME]
        match = float(align[AlignmentTableCreator.MATCH_COL_NAME])
        mismatch = float(align[AlignmentTableCreator.MISMATCH_COL_NAME])
        gap = float(align[AlignmentTableCreator.GAP_COL_NAME])
        alignment = Alignment(Sequence(seq1Id, seq1), Sequence(seq2Id, seq2), Scoring(match, mismatch, gap), seq1Aligned, seq2Aligned)
        return alignment





