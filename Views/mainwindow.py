from typing import List

from Views.ui_mainwindow import *
import resources.res


class MainWindow(QMainWindow):

    scoring_selected = Signal(str, str, str)
    dotplot_process_clicked = Signal()
    alignment_process_clicked = Signal()
    fetch_seq_clicked = Signal()
    seq_selected = Signal(int, str)
    process_double_clicked = Signal(int)
    window_minimized = Signal()
    window_closed = Signal()
    drag_and_drop_accepted = Signal(QMimeData)

    __BLINK_DURATION = 500

    __OK_KEY = "ok"
    __LED_OK_STYLESHEET = ":/green_led.png"
    __IDLE_KEY = "idle"
    __LED_IDLE_STYLESHEET = ":/orange_led.png"
    __WRONG_KEY = "wrong"
    __LED_WRONG_STYLESHEET = ":/red_led.png"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Alignment")
        self._connectSlots()
        self._ledBlinking = {1: False, 2: False, 3: False}
        QTimer.singleShot(50, lambda: self.setDefaultIcons())

    def changeEvent(self, event: QEvent) -> None:
        if self.windowState() == Qt.WindowMinimized:
            self.window_minimized.emit()

    def show(self) -> None:
        super().show()
        if self.parent() is not None and self.parent() is not ...:
            self.parent().show()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.window_closed.emit()

    def addSequences(self, seqIds: List[str]):
        for id in seqIds:
            self.newSeqAvailable(id)

    def setDefaultIcons(self):
        self._setLedStyleSheet(1, MainWindow.__IDLE_KEY)
        self._setLedStyleSheet(2, MainWindow.__IDLE_KEY)
        self._setLedStyleSheet(3, MainWindow.__IDLE_KEY)

    def _connectSlots(self):
        self.ui.selectSeqFirstBtn.clicked.connect(self._firstSeqSelected)
        self.ui.selectSeqSecBtn.clicked.connect(self._secSeqSelected)
        self.ui.fetchScoringBtn.clicked.connect(self._scoringSelected)
        self.ui.processBtn.clicked.connect(self._processBtnClicked)
        self.ui.seqFromNetAction.triggered.connect(self.fetch_seq_clicked)

    def _setLedStyleSheet(self, led, style):
        st = QPixmap()
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
            lbl.setPixmap(QPixmap(st).scaled(lbl.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))

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
        seq2Index = self.ui.seq1ListWidget.currentRow()
        if seq2Index >= 0:
            self.seq_selected.emit(2, self.ui.seq1ListWidget.item(seq2Index).text())
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

    def removeSequence(self, id: str):
        index: int = 0
        size = self.ui.seq1ListWidget.count()
        found = False
        while index < size and not found:
            item = self.ui.seq1ListWidget.item(index)
            if item.text() == id:
                self.ui.seq1ListWidget.takeItem(index)
                found = True
            index += 1






