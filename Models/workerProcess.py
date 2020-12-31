from PySide2.QtCore import QProcess, Signal


class WorkerProcess(QProcess):

    task_finished = Signal(int)

    def __init__(self, id, command):
        super().__init__()
        self._command = command
        self._id = id
        self.finished.connect(self.finishedTask)

    def exec(self):
        super().start(self._command)

    def finishedTask(self):
        self.task_finished.emit(self._id)









