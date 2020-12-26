from Models.workerProcess import WorkerProcess
from PySide2.QtCore import Signal, QTimer, QObject
from Models.scoring import Scoring
import psutil


class ProcessController(QObject):

    proc_infos = Signal(dict)
    process_finished = Signal(int)

    __PROCESSES_POOL_SIZE = 4
    __TIMER_INTERVAL = 500

    def __init__(self):
        super().__init__()
        self._processes = dict()
        self._nextProcIndex = 0
        self._procPids = dict()
        self._psutilProcs = dict()
        self._getProcInfoTimer = QTimer()
        self._getProcInfoTimer.timeout.connect(self.getProcInfo)
        self._getProcInfoTimer.start(ProcessController.__TIMER_INTERVAL)

    def createDotplotProcess(self, seq1Id, seq2Id):
        return self._createProcess(f"python Models/dotplotProgram.py $$${str(seq1Id)}$$${str(seq2Id)}")

    def createAlignmentProcess(self, seq1Id, seq2Id, scoring):
        return self._createProcess(f"python Models/alignmentProgram.py $$${str(seq1Id)}$$${str(seq2Id)}$$${scoring.match}$$${scoring.mismatch}$$${scoring.gap}")

    def canCreate(self) -> bool:
        if self._nextProcIndex in self._processes:
            return False
        else:
            return True

    def procExists(self, selectedFirstSeq: str, selectedSecSeq: str, selectedScoring: Scoring):
        return False

    def procExists(self, selectedFirstSeq, selectedSecSeq):
        return False

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
                    info = dict()
                    info["id"] = self._procIdFromPid(proc.pid)
                    info["pid"] = proc.pid
                    info["cpu"] = proc.cpu_percent()/psutil.cpu_count()
                    info["status"] = proc.status()
                    info["mem"] = proc.memory_percent()
                    self.proc_infos.emit(info)
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
            self._nextProcIndex = (self._nextProcIndex + 1) % ProcessController.__PROCESSES_POOL_SIZE
            self._getProcInfoTimer.start(ProcessController.__TIMER_INTERVAL)
            return procId

    def _removeProcess(self, id):
        print("task sie skonczył!!!!", id)
        if id in self._processes:
            self._processes.pop(id)
            self._procPids.pop(id)
            self.process_finished.emit(id)

    def _procIdFromPid(self, pid):
        for id in self._procPids:
            if self._procPids[id] == pid:
                return id
        return -1









