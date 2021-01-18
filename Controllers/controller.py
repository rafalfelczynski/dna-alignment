from PySide2.QtNetwork import QNetworkAccessManager

from Controllers.alignmentDndHandler import AlignmentDndHandler
from Controllers.dndHandler import DragAndDropHandler
from Controllers.netConnChecker import InternetConnectionChecker
from Controllers.processController import ProcessController
from Controllers.resultsController import ResultsController
from Controllers.seqDialogController import SeqDialogController
from Controllers.sequenceDragAndDropHandler import SequenceDragAndDropHandler
from Models.Database.databaseCreator import DatabaseCreator
from Models.Database.dbconnection import DBConnection
from Models.Database.sequenceDbProvider import SequenceDbProvider
from Models.Database.sequenceRepository import SequenceRepository
from Models.Database.dotplotDbProvider import DotplotDbProvider
from Models.Database.dotplotRepository import DotplotRepository
from Models.Database.alignmentDbProvider import AlignmentDbProvider
from Models.Database.alignmentRepository import AlignmentRepository
from Models.scoring import Scoring
from Models.sequenceManager import SeqManager
from Views.autoPosMenu import AutoPosMenu
from Views.infoDialog import InfoDialog
from Views.mainwindow import MainWindow
from Views.resultsWidget import ResultsWidget
from Views.openglwidget import *
from Models.objLoader import *

import resources.res


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
    objfile = ":/helix.obj"

    def __init__(self):
        super().__init__()
        self.backgroundWidget = MyOpenGLWidget()
        lay = QGridLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        self.backgroundWidget.setLayout(lay)
        objloader = ObjLoader()
        obj3d = objloader.loadObj(self.objfile)
        self.backgroundWidget.setObject3D(obj3d)
        self.backgroundWidget.startAnimation(45)
        self._dbConnection = DBConnection()
        DatabaseCreator.createDatabase(self._dbConnection)
        self._dotpProvider = DotplotDbProvider(self._dbConnection)
        self._alignProvider = AlignmentDbProvider(self._dbConnection)
        self._seqProvider = SequenceDbProvider(self._dbConnection)
        self.mainWindow = MainWindow(self.backgroundWidget)
        lay.addWidget(self.mainWindow)
        self.mainWindow.setWindowFlag(Qt.Window, False)
        self.parentDummy = QWidget()
        self._centralWidgetMemory = ...
        self.resultsWidget = ResultsWidget()
        self.resultsController = ResultsController(self.resultsWidget,
                                                   DotplotRepository(self._dotpProvider),
                                                   AlignmentRepository(self._alignProvider),
                                                   AlignmentDndHandler(AlignmentRepository(self._alignProvider)))
        self.resultsController.screenshot_saved.connect(self._displaySystemTrayMessage)
        self.operationWidget = self.mainWindow.centralWidget()
        self._networkManager = QNetworkAccessManager()
        self._internetConnectionChecker = InternetConnectionChecker(self._networkManager)
        self._internetConnectionChecker.setConnectionGraphicsView(self.mainWindow.ui.internetConnLbl)
        self._internetConnectionChecker.startChecking()
        self.procContr: ProcessController = ProcessController(self.mainWindow.ui.activeProcTableWidget,
                                                              DotplotRepository(self._dotpProvider),
                                                              AlignmentRepository(self._alignProvider))
        self.procContr.process_created.connect(self._releaseSelectedData)
        self.procContr.process_finished.connect(self._processFinished)
        self.seqManager = SeqManager(self._networkManager, SequenceRepository(self._seqProvider))
        self.dialogContr = SeqDialogController(self.seqManager)
        self._dndHandler: DragAndDropHandler = SequenceDragAndDropHandler(self.mainWindow,
                                                                          SequenceRepository(self._seqProvider))
        self.connectMainWindow()
        self.connectSeqManager()
        self._loadSequences()
        self.backgroundWidget.resize(self.mainWindow.size())
        self.backgroundWidget.show()
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
        self.backgroundWidget.window_minimized.connect(self._foldToSystemTray)
        self.backgroundWidget.window_closed.connect(self._foldToSystemTray)
        self.mainWindow.ui.seq1ListWidget.item_dropped.connect(self._dndHandler.parseDroppedItems)
        self.mainWindow.ui.seq1ListWidget.item_dragged.connect(self._dndHandler.exportDraggedItem)
        self.mainWindow.ui.seq1ListWidget.item_double_clicked.connect(self.seqManager.showSequence)
        self.mainWindow.ui.seq1ListWidget.item_right_clicked.connect(self.seqManager.removeSequence)
        self.seqManager.seq_removed.connect(self.mainWindow.removeSequence)
        self.mainWindow.ui.viewResultsAction.triggered.connect(self._resultsViewClicked)
        self.mainWindow.ui.viewOperationAction.triggered.connect(self._operationViewClicked)
        self.mainWindow.ui.helpAboutAction.triggered.connect(self._showHelpInfoDialog)

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

    def _displaySystemTrayMessage(self, title, msg):
        self._sysTrayIcon.showMessage(title, msg, msecs=500)

    def connectSeqManager(self):
        self.seqManager.new_seq_available.connect(self.mainWindow.newSeqAvailable)

    def createDotplotProcess(self):
        if self._checkIfAllSelectedForDotplot():
            self.procContr.createDotplotProcess(self._selectedFirstSeq, self._selectedSecSeq)

    def createAlignmentProcess(self):
        if self._checkIfAllSelectedForAlignment():
            self.procContr.createAlignmentProcess(self._selectedFirstSeq, self._selectedSecSeq, self._selectedScoring)

    def showInfoDialog(self, msg: str, width, height):
        dialog = InfoDialog()
        dialog.resize(width, height)
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
        self._internetConnectionChecker.stopChecking()
        self.backgroundWidget.hide()
        self.mainWindow.hide()

    def _restoreFromSystemTray(self):
        self.mainWindow.show()
        self.backgroundWidget.showNormal()
        self.backgroundWidget.activateWindow()
        self._internetConnectionChecker.startChecking()

    def _closeResourcesAndQuit(self):
        self._dbConnection.close()
        self.procContr.killAll()
        self.finished.emit()

    def _resultsViewClicked(self):
        if self.resultsWidget != self.mainWindow.centralWidget():
            self.mainWindow.centralWidget().setParent(self.parentDummy)
            self.mainWindow.setCentralWidget(self.resultsWidget)

    def _operationViewClicked(self):
        if self.operationWidget != self.mainWindow.centralWidget():
            self.mainWindow.centralWidget().setParent(self.parentDummy)
            self.mainWindow.setCentralWidget(self.operationWidget)

    def _processFinished(self, id):
        if self.backgroundWidget.isHidden():
            self._displaySystemTrayMessage("Process finished", "One of your tasks has just finished processing")

    def _showHelpInfoDialog(self):
        msg = "This application allows you to create a Dotplot and an Alignment from any 2 of the DNA sequences.\n" \
              "You can fetch sequence from the Internet by clicking a button in top-left corner or " \
              'you can simply drag and drop files onto "Sequences" area.' \
              " If you don't have the internet connection enabled, you will se a blue wifi icon with red cross on it" \
              "and you won't be able to fetch any sequence from the internet.\n" \
              'Dropped file has to contain a sequence in fasta format, which means it has to have some sort of' \
              ' identifier following ">" character.' \
              ' After the identifier and space character there may be some comments.' \
              ' Starting from the new line there should be appropriate sequence and it can occupy multiple lines.\n' \
              'You can also copy the sequence onto your computer byt dragging it and dropping onto you system files. ' \
              'It will be saved in fasta format. ' \
              'If some sequences have been obtained, you can select two sequences to create a Dotplot or an Alignment.' \
              'After selecting each sequence, the related led should indicate successful selection.' \
              'To create a Dotplot you need only 2 sequences but to make an Alignment, you also need to define a scoring,' \
              ' that will be used to calculate the alignment. Different scoring values can produce different results.' \
              'Type in the values you want in proper fields and click "Select" button.\n' \
              'Dotplot or alignment processing can be time consuming and CPU expensive,' \
              ' so you can create up to 4 different operations independently. ' \
              'Each operation is then represented as a running process which can be stopped (killed) by double clicking it in table.' \
              ' You can minimize or close the window without any risks. App will be still running in the background' \
              ' and can be restored by double clicking the app icon in your system tray.' \
              ' After the operation finishes successfully and the app is minimized,' \
              ' you will be notified about it if you have system notifications enabled.\n' \
              'You can check any of the obtained results by changing the View to "Results" by clicking ' \
              'an appropriate button on the app menu.\n' \
              'If already in the results view, you can double click a dotplot or an alignment to see the proper results.' \
              'If you select a Dotplot, it will be open in separate window, ' \
              'where you can drag the chart or zoom in and out to see more details. ' \
              'By pressing the SPACE on your keyboard, you can make a snapshot of' \
              ' currently selected fragment of the chart to analyze it later.\n' \
              'Images are stored in the directory: <user>/Documents/alignment/' \
              '\nAlignments can be copied from the Application onto your computer machine by simply selecting a row and' \
              ' dragging it onto yor system files. ' \
              'The generated file will also contain some simple analysis of the alignment.' \
              '\n\nContact to the author: Rafał Felczyński, 236809@student.pwr.edu.pl'
        self.showInfoDialog(msg, 600, 400)











