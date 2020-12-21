from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Views.mainwindow import *
from processController import *
from datetime import datetime


def isFloat(num):
    num = str(num).replace(",", ".")
    try:
        float(num)
        return True
    except ValueError:
        return False


class Controller:

    def __init__(self, procContr):
        self.procContr: ProcessController = procContr
        self.procContr.proc_infos.connect(self.procInfosReceived)
        self.procContr.process_finished.connect(self.removeProcessFromList)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.mainWindow.validate_scoring.connect(self.validateClick)
        self.mainWindow.dotplot_process_clicked.connect(self.createDotplotProcess)
        self.mainWindow.alignment_process_clicked.connect(self.createAlignmentProcess)

    def createDotplotProcess(self, seq1, seq2, scoring):
        procId = self.procContr.createAlignmentProcess(seq1, seq2, scoring)
        self._createProcess(procId)

    def createAlignmentProcess(self, seq1, seq2, scoring):
        procId = self.procContr.createDotplotProcess(seq1, seq2, scoring)
        self._createProcess(procId)

    def _createProcess(self, procId):
        if procId >= 0:
            # self.mainWindow.uncheckSequences()
            self.procContr.executeProcess(procId)
            self.mainWindow.addProcess(procId, self.procContr.procPidFromId(procId), datetime.now(), seq1, seq2)

    def procInfosReceived(self, processes: dict):
        self.mainWindow.updateProcessData(processes["id"], processes["cpu"], processes["mem"])

    def removeProcessFromList(self, id):
        self.mainWindow.removeProcess(id)

    def validateClick(self, match, mismatch, gap):
        isOk = False
        if isFloat(match) \
                and isFloat(mismatch) \
                and isFloat(gap):
            isOk = True
        if isOk:
            self.mainWindow.scoringClickValidatedOk()
        else:
            self.mainWindow.scoringClickValidatedWrong()









