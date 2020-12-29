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
        self.setItem(rowPosition, 0, self.__createTableCell(id))
        self.setItem(rowPosition, 1, self.__createTableCell(pid))
        self.setItem(rowPosition, 2, self.__createTableCell(date))
        self.setItem(rowPosition, 3, self.__createTableCell(seq1id))
        self.setItem(rowPosition, 4, self.__createTableCell(seq2id))
        if scoring is not None:
            self.setItem(rowPosition, 5, self.__createTableCell(scoring.match))
            self.setItem(rowPosition, 6, self.__createTableCell(scoring.mismatch))
            self.setItem(rowPosition, 7, self.__createTableCell(scoring.gap))
        else:
            self.setItem(rowPosition, 5, self.__createTableCell("None"))
            self.setItem(rowPosition, 6, self.__createTableCell("None"))
            self.setItem(rowPosition, 7, self.__createTableCell("None"))
        for i in range(7, cols):
            self.setItem(cols - 1, i, self.__createTableCell(""))

    def __createTableCell(self, text):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def updateProcessData(self, id, pid, cpu, mem):
        row = self._rowOfProcessOfId(id)
        if row >= 0:
            self.setItem(row, 1, self.__createTableCell(pid))
            self.setItem(row, 8, self.__createTableCell(f"{cpu:3.2}"))
            self.setItem(row, 9, self.__createTableCell(f"{mem:3.2}"))

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

    def checkIfProcExists(self, selectedFirstSeq, selectedSecSeq, selectedScoring: Scoring):
        for i in range(0, self.rowCount()):
            seq1id = self.item(i, 3).text()
            seq2id = self.item(i, 4).text()
            doSeqsMatch: bool = selectedFirstSeq == seq1id and selectedSecSeq == seq2id
            if selectedScoring is None:
                return doSeqsMatch
            else:
                match = self.item(i, 5).text()
                mismatch = self.item(i, 6).text()
                gap = self.item(i, 7).text()
                return doSeqsMatch \
                       and str(selectedScoring.match) == match \
                       and str(selectedScoring.mismatch) == mismatch \
                       and str(selectedScoring.gap) == gap
