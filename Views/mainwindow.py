from Views.ui_mainwindow import *
from typing import List
from Models.scoring import Scoring
from PySide2.QtGui import QFocusEvent, QCloseEvent
from PySide2.QtCore import QEvent
from PySide2.QtWidgets import QWidget


class MainWindow(QMainWindow):

    scoring_selected = Signal(str, str, str)
    dotplot_process_clicked = Signal()
    alignment_process_clicked = Signal()
    fetch_seq_clicked = Signal()
    seq_selected = Signal(int, str)
    process_double_clicked = Signal(int)
    window_minimized = Signal()
    window_closed = Signal()

    __BLINK_DURATION = 500

    __OK_KEY = "ok"
    __LED_OK_STYLESHEET = "QLabel { border-radius: 10px;" \
                          " background-color: rgba(64, 255, 0, 200);" \
                          " border: 3px solid black;" \
                          " color: black;" \
                          " }"
    __IDLE_KEY = "idle"
    __LED_IDLE_STYLESHEET = "QLabel { border-radius: 10px;" \
                            " border: 3px solid black;" \
                            " background-color: rgba(255, 173, 51, 200);" \
                            " color: black;" \
                            " }"
    __WRONG_KEY = "wrong"
    __LED_WRONG_STYLESHEET = "QLabel { border-radius: 10px;" \
                             " border: 3px solid black;" \
                             " background-color: rgba(255, 0, 0, 200);" \
                             " color: black;" \
                             " }"

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._connectSlots()
        self.ui.activeProcTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self._ledBlinking = {1: False, 2: False, 3: False}

    def changeEvent(self, event: QEvent) -> None:
        if self.windowState() == Qt.WindowMinimized:
            self.window_minimized.emit()

    def closeEvent(self, event: QCloseEvent) -> None:
        print("closed")
        self.window_closed.emit()

    def addSequences(self, seqIds: List[str]):
        for id in seqIds:
            self.newSeqAvailable(id)

    def uncheckSequences(self):
        # Uncheck each sequence in list view...
        self._setLedStyleSheet(1, MainWindow.__IDLE_KEY)
        self._setLedStyleSheet(2, MainWindow.__IDLE_KEY)

    def addProcess(self, id, pid, date, seq1id, seq2id, scoring: Scoring):
        rowPosition = self.ui.activeProcTableWidget.rowCount()
        self.ui.activeProcTableWidget.insertRow(rowPosition)
        cols = self.ui.activeProcTableWidget.columnCount()
        self.ui.activeProcTableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(id)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(pid)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(date)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(seq1id)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(seq2id)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 5, QTableWidgetItem(str(scoring[Scoring.Keys.Match])))
        self.ui.activeProcTableWidget.setItem(rowPosition, 6, QTableWidgetItem(str(scoring[Scoring.Keys.Mismatch])))
        self.ui.activeProcTableWidget.setItem(rowPosition, 7, QTableWidgetItem(str(scoring[Scoring.Keys.Gap])))
        for i in range(7, cols):
            self.ui.activeProcTableWidget.setItem(cols - 1, i, QTableWidgetItem(""))

    def updateProcessData(self, id, cpu, mem):
        row = self._rowOfProcessOfId(id)
        if row >= 0:
            self.ui.activeProcTableWidget.setItem(row, 8, QTableWidgetItem(f"{cpu:3.2}"))
            self.ui.activeProcTableWidget.setItem(row, 9, QTableWidgetItem(f"{mem:3.2}"))

    def removeProcess(self, id):
        row = self._rowOfProcessOfId(id)
        if row >= 0:
            self.ui.activeProcTableWidget.removeRow(row)

    def _rowOfProcessOfId(self, id):
        for i in range(0, self.ui.activeProcTableWidget.rowCount()):
            rowId = self.ui.activeProcTableWidget.item(i, 0).text()
            if str(id) == rowId:
                return i
        return -1

    def _connectSlots(self):
        self.ui.selectSeqFirstBtn.clicked.connect(self._firstSeqSelected)
        self.ui.selectSeqSecBtn.clicked.connect(self._secSeqSelected)
        self.ui.fetchScoringBtn.clicked.connect(self._scoringSelected)
        self.ui.processBtn.clicked.connect(self._processBtnClicked)
        self.ui.seqFromNetAction.triggered.connect(self.fetch_seq_clicked)
        self.ui.activeProcTableWidget.cellDoubleClicked.connect(self._processDoubleClicked)

    def _setLedStyleSheet(self, led, style):
        st = ""
        if style == MainWindow.__OK_KEY:
            st = self.__LED_OK_STYLESHEET
        elif style == MainWindow.__WRONG_KEY:
            st = self.__LED_WRONG_STYLESHEET
        elif style == MainWindow.__IDLE_KEY:
            st = self.__LED_IDLE_STYLESHEET
        lbl = None
        if led == 1:
            lbl = self.ui.seqFirstLedLbl
        elif led == 2:
            lbl = self.ui.seqSecLedLbl
        elif led == 3:
            lbl = self.ui.scoringLedLbl
        if lbl is not None:
            lbl.setStyleSheet(st)

    def scoringClickValidatedOk(self):
        self._ledBlinking[3] = False
        self._setLedStyleSheet(3, MainWindow.__OK_KEY)

    def scoringClickValidatedWrong(self):
        self._setLedStyleSheet(3, MainWindow.__WRONG_KEY)
        self.blinkLed(3)

    def _firstSeqSelected(self):
        seq1Index = self.ui.seq1ListWidget.currentRow()
        if seq1Index >= 0:
            self.seq_selected.emit(1, self.ui.seq1ListWidget.item(seq1Index).text())
            self._ledBlinking[1] = False
            self._setLedStyleSheet(1, MainWindow.__OK_KEY)
        else:
            self.seq_selected.emit(1, None)
            self._setLedStyleSheet(1, MainWindow.__WRONG_KEY)
            self.blinkLed(1)

    def _secSeqSelected(self):
        seq2Index = self.ui.seq2ListWidget.currentRow()
        if seq2Index >= 0:
            self.seq_selected.emit(2, self.ui.seq2ListWidget.item(seq2Index).text())
            self._ledBlinking[2] = False
            self._setLedStyleSheet(2, MainWindow.__OK_KEY)
        else:
            self.seq_selected.emit(2, None)
            self._setLedStyleSheet(2, MainWindow.__WRONG_KEY)
            self.blinkLed(2)

    def _scoringSelected(self):
        self.scoring_selected.emit(self.ui.matchLineEdit.text(),
                                   self.ui.mismatchLineEdit.text(),
                                   self.ui.gapLineEdit.text())

    def _processBtnClicked(self):
        if self.ui.dotplotRadioBtn.isChecked():
            self.dotplot_process_clicked.emit()
        else:
            self.alignment_process_clicked.emit()

    def blinkLed(self, led):
        def blink(counter, maximum):
            if self._ledBlinking[led]:
                if counter >= maximum:
                    self._stoppedBlinking(led)
                elif counter % 2 == 0:
                    self._setLedStyleSheet(led, MainWindow.__WRONG_KEY)
                    QTimer.singleShot(self.__BLINK_DURATION, lambda: blink(counter + 1, maximum))
                else:
                    self._setLedStyleSheet(led, MainWindow.__IDLE_KEY)
                    QTimer.singleShot(self.__BLINK_DURATION, lambda: blink(counter + 1, maximum))
        if not self._ledBlinking[led]:
            self._ledBlinking[led] = True
            blink(0, 6)

    def _stoppedBlinking(self, led):
        self._ledBlinking[led] = False

    def newSeqAvailable(self, id: str):
        self.ui.seq1ListWidget.addItem(id)
        self.ui.seq2ListWidget.addItem(id)

    def _processDoubleClicked(self, row: int, column: int):
        print("id:", int(self.ui.activeProcTableWidget.item(row, 0).text()))
        self.process_double_clicked.emit(int(self.ui.activeProcTableWidget.item(row, 0).text()))






