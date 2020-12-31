from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Models.alignment import Alignment
from typing import List
from Models.sequence import Sequence
from Models.scoring import Scoring


class AlignmentsTableWidget(QTableWidget):

    __START_DRAG_DISTANCE = 30
    item_dragged = Signal(str, QObject)
    item_dropped = Signal(QMimeData)
    item_double_clicked = Signal(str)
    item_right_clicked = Signal(str)

    alignment_double_clicked = Signal(Alignment)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSelectionMode(QHeaderView.NoSelection)
        self.cellDoubleClicked.connect(self._alignmentDoubleClicked)
        self.setAcceptDrops(False)
        self._dragStartPos: QPoint = ...

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._dragStartPos = event.pos()
        elif event.button() == Qt.MouseButton.RightButton:
            row = self._parseClickedItem(event.pos())
            if row is not None:
                seq1Id, seq2Id, match, mismatch, gap = row
                self.item_right_clicked.emit(f"{seq1Id}$$${seq2Id}$$${match}$$${mismatch}$$${gap}")
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if Qt.MouseButton.LeftButton == event.buttons():
            if (event.pos() - self._dragStartPos).manhattanLength() > self.__START_DRAG_DISTANCE:
                item = self.convertDraggedItemToString()
                if item:
                    self.item_dragged.emit(item, QObject())

    def convertDraggedItemToString(self) -> str:
        row = self._parseClickedItem(self._dragStartPos)
        if row is not None:
            seq1id, seq2id, match, mismatch, gap = row
            return f"{seq1id}$$${seq2id}$$${match}$$${mismatch}$$${gap}"
        else:
            return ""

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
        seq1id, seq2id, match, mismatch, gap = self._parseClickedRow(row)
        scoring = Scoring(float(match), float(mismatch), float(gap))
        alignment = Alignment(Sequence(seq1id, None), Sequence(seq2id, None), scoring)
        self.alignment_double_clicked.emit(alignment)

    def _parseClickedItem(self, position):
        clickedItem = self.itemAt(position)
        if clickedItem is not None:
            return self._parseClickedRow(clickedItem.row())
        return None

    def _parseClickedRow(self, row):
        if row >= 0:
            seq1id = self.item(row, 0).text()
            seq2id = self.item(row, 1).text()
            match = self.item(row, 2).text()
            mismatch = self.item(row, 3).text()
            gap = self.item(row, 4).text()
            return seq1id, seq2id, match, mismatch, gap
        return None


