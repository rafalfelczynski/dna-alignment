from workerProcess import WorkerProcess


class ProcessController:

    __PROCESSES_POOL_SIZE = 4

    def __init__(self):
        self._processes = dict()
        self._nextProcIndex = 0

    def createProcess(self, command) -> int:
        if not self.canCreate():
            return -1
        else:
            proc = WorkerProcess(command)
            procId = self._nextProcIndex
            self._processes[procId] = proc
            self._nextProcIndex = (self._nextProcIndex + 1) % ProcessController.__PROCESSES_POOL_SIZE
            return procId

    def canCreate(self) -> bool:
        if self._nextProcIndex in self._processes:
            return False
        else:
            return True

    def executeProcess(self, id, command):
        pass








