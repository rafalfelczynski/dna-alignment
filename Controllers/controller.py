from PySide2.QtGui import QIcon, QDragEnterEvent, QDrag, QPixmap
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Views.mainwindow import MainWindow
from Controllers.processController import ProcessController
from datetime import datetime
from Controllers.seqDialogController import SeqDialogController
from Models.sequenceManager import SeqManager
from Models.Database.seqReader import SeqDBReader
from Models.Database.seqTableCreator import SequencesTableCreator
from Models.Database.seqDbWriter import SeqDBWriter
from Models.Database.dbconnection import DBConnection
from PySide2.QtNetwork import QNetworkAccessManager
from Models.scoring import Scoring
from Models.Database.databaseCreator import DatabaseCreator
from Views.infoDialog import InfoDialog
from Views.confirmDialog import ConfirmDialog
from PySide2.QtCore import Signal
from Views.autoPosMenu import AutoPosMenu
from Models.fileFastaReader import *
from typing import List
from Controllers.dndFileParser import DnDFileParser
import resources.res
from Controllers.dndHandler import DragAndDropHandler
from Controllers.sequenceDragAndDropHandler import SequenceDragAndDropHandler
from Models.Database.seqDbUpdater import SeqDbUpdater
from Controllers.netConnChecker import InternetConnectionChecker
from Models.Database.dotplotReader import DotplotReader
from Models.Database.alignmentReader import AlignmentReader
from Views.resultsWidget import ResultsWidget
from Controllers.resultsController import ResultsController


def isFloat(num):
    num = str(num).replace(",", ".")
    try:
        float(num)
        return True
    except ValueError:
        return False


class Controller(QObject):

    finished = Signal()

    __SYSTEM_TRAY_ICON = ":/dna_icon.png"

    def __init__(self):
        super().__init__()
        self._dbConnection = DBConnection()
        DatabaseCreator.createDatabase(self._dbConnection)
        self._dotplotReader = DotplotReader(self._dbConnection)
        self._alignReader = AlignmentReader(self._dbConnection)
        self.seqDbReader = SeqDBReader(self._dbConnection)
        self.seqDbWriter = SeqDBWriter(self._dbConnection)
        self.mainWindow = MainWindow()
        self.parentDummy = QWidget()
        self._centralWidgetMemory = ...
        self.resultsWidget = ResultsWidget()
        self.resultsController = ResultsController(self.resultsWidget, self._dotplotReader, self._alignReader)
        self.operationWidget = self.mainWindow.centralWidget()
        self._networkManager = QNetworkAccessManager()
        self._internetConnectionChecker = InternetConnectionChecker(self._networkManager)
        self._internetConnectionChecker.setConnectionGraphicsView(self.mainWindow.ui.internetConnLbl)
        self._internetConnectionChecker.startChecking()
        self.procContr: ProcessController = ProcessController(self.mainWindow.ui.activeProcTableWidget, self._dotplotReader, self._alignReader)
        self.procContr.process_created.connect(self._releaseSelectedData)
        self.seqManager = SeqManager(self._networkManager, self.seqDbReader, self.seqDbWriter, SeqDbUpdater(self._dbConnection))
        self.dialogContr = SeqDialogController(self.seqManager)
        self._dndHandler: DragAndDropHandler = SequenceDragAndDropHandler(self.mainWindow, self.seqDbReader, self.seqDbWriter)
        self.connectMainWindow()
        self.connectSeqManager()
        self._loadSequences()
        self.mainWindow.show()
        self._selectedScoring: Scoring = None
        self._selectedFirstSeq: str = None
        self._selectedSecSeq: str = None
        self._sysTrayIcon: QSystemTrayIcon = ...
        self._sysTrayIconMenu: QMenu = ...
        self._createSystemTrayIcon()
        self._sysTrayIcon.show()

    def connectMainWindow(self):
        self.mainWindow.scoring_selected.connect(self.validateScoring)
        self.mainWindow.dotplot_process_clicked.connect(self.createDotplotProcess)
        self.mainWindow.alignment_process_clicked.connect(self.createAlignmentProcess)
        self.mainWindow.fetch_seq_clicked.connect(self._fetchFromInternetClicked)
        self.mainWindow.seq_selected.connect(self._seqSelected)
        self.mainWindow.window_minimized.connect(self._foldToSystemTray)
        self.mainWindow.window_closed.connect(self._foldToSystemTray)
        self.mainWindow.ui.seq1ListWidget.item_dropped.connect(self._dndHandler.parseDroppedItems)
        self.mainWindow.ui.seq1ListWidget.item_dragged.connect(self._dndHandler.exportDraggedItem)
        self.mainWindow.ui.seq1ListWidget.item_double_clicked.connect(self.seqManager.showSequence)
        self.mainWindow.ui.seq1ListWidget.item_right_clicked.connect(self.seqManager.removeSequence)
        self.seqManager.seq_removed.connect(self.mainWindow.removeSequence)
        self.mainWindow.ui.viewResultsAction.triggered.connect(self._resultsViewClicked)
        self.mainWindow.ui.viewOperationAction.triggered.connect(self._operationViewClicked)

    def _createSystemTrayIcon(self):
        self._sysTrayIcon = QSystemTrayIcon()
        self._sysTrayIcon.setIcon(QIcon(Controller.__SYSTEM_TRAY_ICON))
        self._createSystemTrayIconMenu()
        self._sysTrayIcon.activated.connect(self._systemTrayIconClicked)
        self._sysTrayIcon.setToolTip("DNA alignment application")

    def _createSystemTrayIconMenu(self):
        self._sysTrayIconMenu = AutoPosMenu()
        quitAction = QAction("Quit", self._sysTrayIconMenu)
        quitAction.triggered.connect(self._closeResourcesAndQuit)
        self._sysTrayIconMenu.addAction(quitAction)
        self._sysTrayIcon.setContextMenu(self._sysTrayIconMenu)

    def _systemTrayIconClicked(self, reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.DoubleClick:
            self._restoreFromSystemTray()

    def connectSeqManager(self):
        self.seqManager.new_seq_available.connect(self.mainWindow.newSeqAvailable)

    def createDotplotProcess(self):
        if self._checkIfAllSelectedForDotplot():
            self.procContr.createDotplotProcess(self._selectedFirstSeq, self._selectedSecSeq)

    def createAlignmentProcess(self):
        if self._checkIfAllSelectedForAlignment():
            self.procContr.createAlignmentProcess(self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring)

    def showInfoDialog(self, msg: str):
        dialog = InfoDialog()
        dialog.setText(msg)
        dialog.exec_()

    def _checkIfAllSelectedForDotplot(self):
        seqOk = True
        if self._selectedFirstSeq == "" or self._selectedFirstSeq is None:
            seqOk = False
            self.mainWindow.blinkLed(1)
        if self._selectedSecSeq == "" or self._selectedSecSeq is None:
            seqOk = False
            self.mainWindow.blinkLed(2)
        return seqOk

    def _checkIfAllSelectedForAlignment(self):
        seqOk = self._checkIfAllSelectedForDotplot()
        scoringOk = True
        if self._selectedScoring is None:
            scoringOk = False
            self.mainWindow.blinkLed(3)
        return seqOk and scoringOk

    def _releaseSelectedData(self):
        self._selectedScoring: Scoring = None
        self._selectedFirstSeq: str = None
        self._selectedSecSeq: str = None
        self.mainWindow.setDefaultIcons()

    def validateScoring(self, match, mismatch, gap):
        isOk = isFloat(match) and isFloat(mismatch) and isFloat(gap)
        if isOk:
            self._selectedScoring = Scoring(float(match), float(mismatch), float(gap))
            self.mainWindow.scoringClickValidatedOk()
        else:
            self._selectedScoring = None
            self.mainWindow.scoringClickValidatedWrong()

    def _loadSequences(self):
        self.mainWindow.addSequences([seq.identifier for seq in self.seqManager.getAllSeqs()])

    def _seqSelected(self, seqNr: int, id: str):
        if seqNr == 1:
            self._selectedFirstSeq = id
        elif seqNr == 2:
            self._selectedSecSeq = id

    def _fetchFromInternetClicked(self):
        if self._internetConnectionChecker.isConnectionWorking():
            self.dialogContr.showDialog()
        else:
            dialog = InfoDialog()
            dialog.setText("There is a problem with your internet connection!")
            dialog.resize(300, 100)
            dialog.exec_()

    def _foldToSystemTray(self):
        self._sysTrayIcon.show()
        self._internetConnectionChecker.stopChecking()
        self.mainWindow.hide()

    def _restoreFromSystemTray(self):
        self.mainWindow.show()
        self._internetConnectionChecker.startChecking()

    def _closeResourcesAndQuit(self):
        # Save data to database if needed, kill all running processes and quit
        self._dbConnection.close()
        self.finished.emit()

    def _resultsViewClicked(self):
        if self.resultsWidget != self.mainWindow.centralWidget():
            self.mainWindow.centralWidget().setParent(self.parentDummy)
            self.mainWindow.setCentralWidget(self.resultsWidget)

    def _operationViewClicked(self):
        if self.operationWidget != self.mainWindow.centralWidget():
            self.mainWindow.centralWidget().setParent(self.parentDummy)
            self.mainWindow.setCentralWidget(self.operationWidget)











