from PySide2.QtCore import QMimeData
from Models.fileFastaReader import *


class DnDFileParser:

    def __init__(self):
        self._fileFastaReader = FileFastaReader()
        self._acceptableRegex = QRegExp("(file:///|file://)(.*.(fasta|txt))")

    def parseDraggedItems(self, draggedData: QMimeData):
        fileNames = draggedData.text().splitlines()
        sequences, accepted, rejected = self._parseDraggedFiles(fileNames)
        return sequences, accepted, rejected

    def _parseDraggedFiles(self, files):
        sequences = []
        accepted = []
        rejected = []
        for filePath in files:
            if self.isAcceptable(filePath):
                file = self._acceptableRegex.cap(2)
                sequence = self._fileFastaReader.read(file)
                if sequence is not None and sequence.isValid():
                    sequences.append(sequence)
                    accepted.append(file)
                else:
                    rejected.append(file)
            else:
                regex = QRegExp("(file:///|file://)(.*)")
                regex.indexIn(filePath)
                rejected.append(regex.cap(2))
        return sequences, accepted, rejected

    def isAcceptable(self, filePath: str):
        if self._acceptableRegex.exactMatch(filePath):
            return True
        return False




