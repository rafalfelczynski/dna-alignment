from ui_mainwindow import *


class MainWindow(QMainWindow):

    validate_scoring = Signal(str, str, str)
    dotplot_process_clicked = Signal(str, str, str)
    alignment_process_clicked = Signal(str, str, str)

    __BLINK_DURATION = 500

    __LED_OK_STYLESHEET = "QLabel { border-radius: 10px;" \
                          " background-color: rgba(64, 255, 0, 200);" \
                          " border: 3px solid black;" \
                          " color: black;" \
                          " }"
    __LED_IDLE_STYLESHEET = "QLabel { border-radius: 10px;" \
                            " border: 3px solid black;" \
                            " background-color: rgba(255, 173, 51, 200);" \
                            " color: black;" \
                            " }"
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
        self._selectedFirstSeq: Sequence = None
        self._selectedSecSeq: Sequence = None
        self._selectedScoring = None
        self._ledBlinking = {1: False, 2: False, 3: False}

    def uncheckSequences(self):
        # Uncheck each sequence in list view...
        self._setLedStyleSheet(1, "idle")
        self._setLedStyleSheet(2, "idle")

    def addProcess(self, id, pid, date, seq1id, seq2id):
        rowPosition = self.ui.activeProcTableWidget.rowCount()
        self.ui.activeProcTableWidget.insertRow(rowPosition)
        cols = self.ui.activeProcTableWidget.columnCount()
        self.ui.activeProcTableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(id)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(pid)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(date)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(seq1id)))
        self.ui.activeProcTableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(seq2id)))
        for i in range(3, cols):
            self.ui.activeProcTableWidget.setItem(cols - 1, i, QTableWidgetItem(""))

    def updateProcessData(self, id, cpu, mem):
        row = self._rowOfProcessOfId(id)
        if row >= 0:
            self.ui.activeProcTableWidget.setItem(row, 5, QTableWidgetItem(f"{cpu:3.2}"))
            self.ui.activeProcTableWidget.setItem(row, 6, QTableWidgetItem(f"{mem:3.2}"))

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

    def _setLedStyleSheet(self, led, style):
        st = ""
        if style == "ok":
            st = self.__LED_OK_STYLESHEET
        elif style == "wrong":
            st = self.__LED_WRONG_STYLESHEET
        elif style == "idle":
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
        self._setLedStyleSheet(3, "ok")

    def scoringClickValidatedWrong(self):
        self._setLedStyleSheet(3, "wrong")
        self.__blinkLed(3)

    def _firstSeqSelected(self):
        self._selectedFirstSeq = None
        seq1Index = self.ui.seq1ListWidget.currentRow()
        if seq1Index >= 0:
            self._selectedFirstSeq = self.ui.seq1ListWidget.item(seq1Index).text()
            self._setLedStyleSheet(1, "ok")
        else:
            self._setLedStyleSheet(1, "wrong")
            self.__blinkLed(1)

    def _secSeqSelected(self):
        self._selectedSecSeq = None
        seq2Index = self.ui.seq2ListWidget.currentRow()
        if seq2Index >= 0:
            self._selectedSecSeq = self.ui.seq2ListWidget.item(seq2Index).text()
            self._setLedStyleSheet(2, "ok")
        else:
            self._setLedStyleSheet(2, "wrong")
            self.__blinkLed(2)

    def _scoringSelected(self):
        self._selectedScoring = None
        self.validate_scoring.emit(self.ui.matchLineEdit.text(),
                                   self.ui.mismatchLineEdit.text(),
                                   self.ui.gapLineEdit.text())

    def _processBtnClicked(self):
        allOk = True
        if self._selectedFirstSeq is None:
            allOk = False
            self.__blinkLed(1)
        if self._selectedSecSeq is None:
            allOk = False
            self.__blinkLed(2)
        if self._selectedScoring is None:
            allOk = False
            self.__blinkLed(3)
        if allOk:
            if self.ui.dotplotRadioBtn.isChecked():
                self.dotplot_process_clicked.emit(self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring)
            else:
                self.alignment_process_clicked.emit(self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring)

    def __blinkLed(self, led):
        def blink(counter, max):
            if counter > max:
                return
            else:
                if counter % 2 == 0:
                    QTimer.singleShot(self.__BLINK_DURATION*counter, lambda: (self._setLedStyleSheet(led, "wrong"), self._stoppedBlinking(led) if counter == max else None))
                else:
                    QTimer.singleShot(self.__BLINK_DURATION*counter, lambda: (self._setLedStyleSheet(led, "idle"), self._stoppedBlinking(led) if counter == max else None))
                blink(counter+1, max)
        if not self._ledBlinking[led]:
            print("blinking:", led)
            self._ledBlinking[led] = True
            blink(0, 7)

    def _stoppedBlinking(self, led):
        self._ledBlinking[led] = False





