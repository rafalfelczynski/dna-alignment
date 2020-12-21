from PySide2.QtCore import QFile, QThread, Signal, QObject, QMutex, QMutexLocker


class WorkerThread(QThread):

    data_ready = Signal(str, str)
    file_not_found = Signal(str)
    thread_exit = Signal(int)

    def __init__(self, filePath, identifier):
        super().__init__()
        self._filePath = filePath
        self._identifier = identifier

    def run(self):
        file = QFile(self._filePath)
        if file.open(QFile.ReadOnly):
            identifier = file.readLine().trimmed().data().decode().replace("\n", "").replace("\r", "")
            data = file.readAll().data().decode().replace("\n", "").replace("\r", "")
            self.data_ready.emit(identifier, data)
            return identifier, data
        else:
            self.file_not_found.emit(self._filePath)
        self.thread_exit.emit(self._identifier)


class FileFastaReader(QObject):

    __CANNOT_OPEN_FILE_ERROR: str = "Cannot open selected file"
    data_ready = Signal(str, str)

    def __init__(self):
        super().__init__()
        self._workers = {}
        self._workerCounter: int = 0
        self.__workerLock = QMutex()

    def getData(self, filePath: str):
        file = QFile(filePath)
        if file.open(QFile.ReadOnly):
            identifier = file.readLine().trimmed().data().decode().replace("\n", "").replace("\r", "")
            data = file.readAll().data().decode().replace("\n", "").replace("\r", "")
            self.data_ready.emit(identifier, data)
            return identifier, data
        else:
            raise FileNotFoundError(self.__CANNOT_OPEN_FILE_ERROR + " " + filePath)
            # self.file_not_found.emit(self._filePath)
        #self.thread_exit.emit(self._identifier)
        # _worker = WorkerThread(filePath, self._workerCounter)
        # _worker.data_ready.connect(self.data_ready)
        # _worker.thread_exit.connect(self.__deleteWorker)
        # self._workers[self._workerCounter] = _worker
        # self._workerCounter += 1
        # _worker.run()

    def __deleteWorker(self, workerId):
        locker = QMutexLocker(self.__workerLock)
        self._workers.pop(workerId)



