from PySide2.QtCore import QProcess
import typing
from dotplotDBWriter import *



class WorkerProcess(QProcess):

    def __init__(self, command):
        super().__init__()
        self._command = command
        self.finished.connect(self.finishedTask())

    def exec(self):
        super().start(self._command)
        pass

    def finishedTask(self):
        pass








