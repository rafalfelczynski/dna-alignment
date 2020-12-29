from Models.workerProcess import WorkerProcess
from PySide2.QtCore import Signal, QTimer, QObject
from Models.scoring import Scoring
import psutil
from datetime import datetime
from Views.activeProcTableWidget import ActiveProcTableWidget
from Views.confirmDialog import ConfirmDialog
from Views.infoDialog import InfoDialog
from Models.Database.alignmentReader import AlignmentReader
from Models.Database.dotplotReader import DotplotReader


class ProcessController(QObject):

    process_finished = Signal(int)
    process_created = Signal(int)

    __PROCESSES_POOL_SIZE = 4
    __TIMER_INTERVAL = 500

    def __init__(self, processWidget, dotplotReader, alignmentReader):
        super().__init__()
        self._processes = dict()
        self._nextProcIndex = 0
        self._procPids = dict()
        self._psutilProcs = dict()
        self._activeProcTableWidget: ActiveProcTableWidget = processWidget
        self._activeProcTableWidget.proc_double_clicked.connect(self._processDoubleClicked)
        self._getProcInfoTimer = QTimer()
        self._getProcInfoTimer.timeout.connect(self.getProcInfo)
        self._getProcInfoTimer.start(ProcessController.__TIMER_INTERVAL)
        self._dotplotReader: DotplotReader = dotplotReader
        self._alignReader: AlignmentReader = alignmentReader

    def createDotplotProcess(self, seq1Id, seq2Id):
        if not self.dotplotProcExists(seq1Id, seq2Id):
            procId = self._createProcess(f"python Models/dotplotProgram.py $$${str(seq1Id)}$$${str(seq2Id)}")
            if procId >= 0:
                self._activeProcTableWidget.addProcess(procId, self.procPidFromId(procId),
                                                       datetime.now(), seq1Id, seq2Id, None)
            return procId
        else:
            dialog = InfoDialog()
            dialog.setText("Dotplot already exists or is currently being created!")
            dialog.resize(300, 200)
            dialog.exec_()

    def createAlignmentProcess(self, seq1Id, seq2Id, scoring):
        if not self.alignmentProcExists(seq1Id, seq2Id, scoring):
            procId = self._createProcess(f"python Models/alignmentProgram.py $$${str(seq1Id)}$$${str(seq2Id)}$$${scoring.match}$$${scoring.mismatch}$$${scoring.gap}")
            if procId >= 0:
                self._activeProcTableWidget.addProcess(procId, self.procPidFromId(procId),
                                                       datetime.now(), seq1Id, seq2Id, scoring)
            return procId
        else:
            dialog = InfoDialog()
            dialog.setText("Alignment already exists or is currently being created!")
            dialog.resize(300, 200)
            dialog.exec_()

    def canCreate(self) -> bool:
        for i in range(0, self.__PROCESSES_POOL_SIZE):
            if i not in self._processes:
                self._nextProcIndex = i
                return True
        return False

    def alignmentProcExists(self, selectedFirstSeq, selectedSecSeq, selectedScoring):
        exists = self._alignReader.checkIfExists(selectedFirstSeq, selectedSecSeq, selectedScoring)
        return exists or self._activeProcTableWidget.checkIfProcExists(selectedFirstSeq, selectedSecSeq, selectedScoring)

    def dotplotProcExists(self, selectedFirstSeq, selectedSecSeq):
        exists = self._dotplotReader.checkIfExists(selectedFirstSeq, selectedSecSeq)
        return exists or self._activeProcTableWidget.checkIfProcExists(selectedFirstSeq, selectedSecSeq, None)

    def executeProcess(self, id):
        if id in self._processes:
            proc: WorkerProcess = self._processes[id]
            proc.exec()
            self._procPids[id] = proc.pid()
            self._psutilProcs[proc.pid()] = psutil.Process(proc.pid())
        else:
            print("proces nie istnieje", id, self._processes.keys())

    def killProcess(self, id):
        if id in self._processes:
            proc: WorkerProcess = self._processes[id]
            if proc.state() == WorkerProcess.ProcessState.Running:
                proc.kill()
                self._removeProcess(id)

    def procPidFromId(self, id):
        if id in self._procPids:
            return self._procPids[id]
        else:
            raise ValueError("ProcessController.procPidFromId :: No such id!")

    def getProcInfo(self):
        if len(self._procPids) > 0:
            for pid in self._psutilProcs:
                if psutil.pid_exists(pid):
                    proc: psutil.Process = self._psutilProcs[pid]
                    id = self._procIdFromPid(proc.pid)
                    cpu = proc.cpu_percent()/psutil.cpu_count()
                    mem = proc.memory_percent()
                    self._activeProcTableWidget.updateProcessData(id, proc.pid, cpu, mem)
                    # self.proc_infos.emit(info)
        else:
            self._getProcInfoTimer.stop()

    def _createProcess(self, command) -> int:
        if not self.canCreate():
            print("Nie stworzono procesu, brak slotów", self._nextProcIndex, self._processes.keys())
            return -1
        else:
            proc = WorkerProcess(self._nextProcIndex, command)
            proc.task_finished.connect(self._removeProcess)
            procId = self._nextProcIndex
            self._processes[procId] = proc
            self._procPids[procId] = proc.pid()
            self._nextProcIndex = (self._nextProcIndex + 1) % ProcessController.__PROCESSES_POOL_SIZE
            self._getProcInfoTimer.start(ProcessController.__TIMER_INTERVAL)
            self.process_created.emit(procId)
            self.executeProcess(procId)
            return procId

    def _removeProcess(self, id):
        print("task sie skonczył!!!!", id, "remove process")
        if id in self._processes:
            pid = self._procPids[id]
            self._psutilProcs.pop(pid)
            self._processes.pop(id)
            self._procPids.pop(id)
            self._activeProcTableWidget.removeProcess(id)
            # self.process_finished.emit(id)

    def _procIdFromPid(self, pid):
        for id in self._procPids:
            if self._procPids[id] == pid:
                return id
        return -1

    def _processDoubleClicked(self, id: int):
        try:
            pid = self.procPidFromId(id)
            dialog = ConfirmDialog()
            dialog.setText(f"Are you sure you want to kill the process with PID {pid}?")
            dialog.resize(300, 100)
            dialog.accepted.connect(lambda: self.killProcess(id))
            dialog.exec_()
        except ValueError as e:
            pass




