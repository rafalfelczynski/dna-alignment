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
from Models.mimeData import MimeData
from Controllers.dndHandler import DragAndDropHandler
from Controllers.sequenceDragAndDropHandler import SequenceDragAndDropHandler
from Models.Database.seqDbUpdater import SeqDbUpdater
from Controllers.netConnChecker import InternetConnectionChecker


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

    def __init__(self, procContr):
        super().__init__()
        self.mainWindow = MainWindow()
        self._networkManager = QNetworkAccessManager()
        self._internetConnectionChecker = InternetConnectionChecker(self._networkManager)
        self._internetConnectionChecker.setConnectionGraphicsView(self.mainWindow.ui.internetConnLbl)
        self._internetConnectionChecker.startChecking()
        self._dbConnection = DBConnection()
        DatabaseCreator.createDatabase(self._dbConnection)
        self.procContr: ProcessController = procContr
        self.procContr.proc_infos.connect(self.procInfosReceived)
        self.procContr.process_finished.connect(self.removeProcessFromList)
        self.seqDbReader = SeqDBReader(self._dbConnection)
        self.seqDbWriter = SeqDBWriter(self._dbConnection)
        self.seqManager = SeqManager(self._networkManager, SeqDBReader(self._dbConnection), SeqDBWriter(self._dbConnection), SeqDbUpdater(self._dbConnection))
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
        self.mainWindow.process_double_clicked.connect(self._processDoubleClicked)
        self.mainWindow.window_minimized.connect(self._foldToSystemTray)
        self.mainWindow.window_closed.connect(self._foldToSystemTray)
        self.mainWindow.ui.seq1ListWidget.item_dropped.connect(self._dndHandler.parseDroppedItems)
        self.mainWindow.ui.seq1ListWidget.item_dragged.connect(self._dndHandler.exportDraggedItem)
        self.mainWindow.ui.seq1ListWidget.item_double_clicked.connect(self.seqManager.showSequence)
        self.mainWindow.ui.seq1ListWidget.item_right_clicked.connect(self.seqManager.removeSequence)
        self.seqManager.seq_removed.connect(self.mainWindow.removeSequence)

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
            if not self.procContr.procExists(self._selectedFirstSeq, self._selectedSecSeq):
                procId = self.procContr.createDotplotProcess(self._selectedFirstSeq, self._selectedSecSeq)
                self._createProcess(procId)

    def createAlignmentProcess(self):
        if self._checkIfAllSelectedForAlignment():
            if not self.procContr.procExists(self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring):
                procId = self.procContr.createAlignmentProcess(self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring)
                self._createProcess(procId)

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

    def _createProcess(self, procId):
        if procId >= 0:
            self.procContr.executeProcess(procId)
            self.mainWindow.addProcess(procId, self.procContr.procPidFromId(procId), datetime.now(), self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring)
            self._releaseSelectedData()

    def _releaseSelectedData(self):
        self._selectedScoring: Scoring = None
        self._selectedFirstSeq: str = None
        self._selectedSecSeq: str = None
        self.mainWindow.setDefaultIcons()

    def procInfosReceived(self, processes: dict):
        self.mainWindow.updateProcessData(processes["id"], processes["cpu"], processes["mem"])

    def removeProcessFromList(self, id):
        self.mainWindow.removeProcess(id)

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

    def _processDoubleClicked(self, id):
        dialog = ConfirmDialog()
        dialog.setText(f"Are you sure you want to kill the process with PID {self.procContr.procPidFromId(id)}?")
        dialog.resize(300, 100)
        dialog.accepted.connect(lambda: self.procContr.killProcess(id))
        dialog.exec_()

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
        self.finished.emit()











