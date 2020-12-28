from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from Models.scoring import Scoring


class ActiveProcTableWidget(QTableWidget):

    proc_double_clicked = Signal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.cellDoubleClicked.connect(lambda r, c: self.proc_double_clicked.emit(int(self.item(r, 0).text())))

    def addProcess(self, id, pid, date, seq1id, seq2id, scoring: Scoring):
        rowPosition = self.rowCount()
        self.insertRow(rowPosition)
        cols = self.columnCount()
        self.setItem(rowPosition, 0, QTableWidgetItem(str(id)))
        self.setItem(rowPosition, 1, QTableWidgetItem(str(pid)))
        self.setItem(rowPosition, 2, QTableWidgetItem(str(date)))
        self.setItem(rowPosition, 3, QTableWidgetItem(str(seq1id)))
        self.setItem(rowPosition, 4, QTableWidgetItem(str(seq2id)))
        if scoring is not None:
            self.setItem(rowPosition, 5, QTableWidgetItem(str(scoring.match)))
            self.setItem(rowPosition, 6, QTableWidgetItem(str(scoring.mismatch)))
            self.setItem(rowPosition, 7, QTableWidgetItem(str(scoring.gap)))
        else:
            self.setItem(rowPosition, 5, QTableWidgetItem("---"))
            self.setItem(rowPosition, 6, QTableWidgetItem("---"))
            self.setItem(rowPosition, 7, QTableWidgetItem("---"))
        for i in range(7, cols):
            self.setItem(cols - 1, i, QTableWidgetItem(""))

    def updateProcessData(self, id, pid, cpu, mem):
        row = self._rowOfProcessOfId(id)
        if row >= 0:
            self.setItem(row, 1, QTableWidgetItem(f"{str(pid)}"))
            self.setItem(row, 8, QTableWidgetItem(f"{cpu:3.2}"))
            self.setItem(row, 9, QTableWidgetItem(f"{mem:3.2}"))

    def removeProcess(self, id):
        row = self._rowOfProcessOfId(id)
        if row >= 0:
            self.removeRow(row)

    def _rowOfProcessOfId(self, id):
        for i in range(0, self.rowCount()):
            rowId = self.item(i, 0).text()
            if str(id) == rowId:
                return i
        return -1




