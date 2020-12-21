from PySide2.QtCore import QProcess, Signal
import typing
from dotplotDBWriter import *


class WorkerProcess(QProcess):

    task_finished = Signal(int)

    def __init__(self, id, command):
        super().__init__()
        self._command = command
        self._id = id
        self.finished.connect(self.finishedTask)

    def exec(self):
        super().start(self._command)
        pass

    def finishedTask(self):
        # Save to database!
        self.task_finished.emit(self._id)
        pass








