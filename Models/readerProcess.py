from PySide2.QtCore import QProcess, Signal, QByteArray
import PySide2
import os


def pr(ident):
    print("identifierrrrrrrr", ident[0])
    print(ident[1])


class ReaderProcess(QProcess):

    results_ready = Signal(str, str)

    def __init__(self, commands):
        super().__init__()
        self.__commands = commands
        self.__index = 0
        self.conn()

    def startFirst(self):
        super().start(self.__commands[self.__index])

    def conn(self):
        self.finished.connect(self.__takeNextCommand)
        self.readyReadStandardError.connect(lambda: print("error", self.readAllStandardError()))

    def __takeNextCommand(self):
        self.__index += 1
        identifier = self.readLine().data().decode()
        data = self.readAll().data().decode()
        self.results_ready.emit(identifier, data)
        if self.__index < len(self.__commands):
            self.start(self.__commands[self.__index])
        else:
            self.close()



