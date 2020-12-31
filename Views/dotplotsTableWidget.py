from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Models.dotplot import Dotplot
from typing import List
from Models.sequence import Sequence


class DotplotsTableWidget(QTableWidget):

    dotplot_double_clicked = Signal(Dotplot)
    item_right_clicked = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.cellDoubleClicked.connect(self._dotplotDoubleClicked)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            item = self.itemAt(event.pos())
            if item is not None:
                seq1Id = self.item(item.row(), 0).text()
                seq2Id = self.item(item.row(), 1).text()
                self.item_right_clicked.emit(f"{seq1Id}$$${seq2Id}")
        super().mousePressEvent(event)

    def refreshData(self, dotplots: List[Dotplot]) -> None:
        for i in range(self.rowCount()-1, -1, -1):
            self.removeRow(i)
        for dotp in dotplots:
            row = self.rowCount()
            self.insertRow(row)
            self.setItem(row, 0, self._createCell(dotp.seq1.identifier))
            self.setItem(row, 1, self._createCell(dotp.seq2.identifier))

    def _createCell(self, text):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def _dotplotDoubleClicked(self, row, col):
        seq1id = self.item(row, 0).text()
        seq2id = self.item(row, 1).text()
        seq1 = Sequence(seq1id, None)
        seq2 = Sequence(seq2id, None)
        self.dotplot_double_clicked.emit(Dotplot(seq1, seq2))





