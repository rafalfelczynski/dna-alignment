from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Models.alignment import Alignment
from typing import List
from Models.sequence import Sequence
from Models.scoring import Scoring


class AlignmentsTableWidget(QTableWidget):

    alignment_double_clicked = Signal(Alignment)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.cellDoubleClicked.connect(self._alignmentDoubleClicked)

    def refreshData(self, aligns: List[Alignment]) -> None:
        for i in range(self.rowCount() - 1, -1, -1):
            self.removeRow(i)
        for al in aligns:
            row = self.rowCount()
            self.insertRow(row)
            self.setItem(row, 0, self._createCell(al.seq1.identifier))
            self.setItem(row, 1, self._createCell(al.seq2.identifier))
            self.setItem(row, 2, self._createCell(al.scoring.match))
            self.setItem(row, 3, self._createCell(al.scoring.mismatch))
            self.setItem(row, 4, self._createCell(al.scoring.gap))

    def _createCell(self, text):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def _alignmentDoubleClicked(self, row, col):
        seq1id = self.item(row, 0).text()
        seq2id = self.item(row, 1).text()
        match = self.item(row, 2).text()
        mismatch = self.item(row, 3).text()
        gap = self.item(row, 4).text()
        seq1 = Sequence(seq1id, None)
        seq2 = Sequence(seq2id, None)
        scoring = Scoring(float(match), float(mismatch), float(gap))
        alignment = Alignment(seq1, seq2, scoring)
        self.alignment_double_clicked.emit(alignment)


