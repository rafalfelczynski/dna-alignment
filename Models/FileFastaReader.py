from PySide2.QtCore import QFile, Signal, QObject, QRegExp

from Models.sequence import Sequence


class NotAFastaFileException(Exception):
    def __init__(self, msg="File does not contain information in fasta format"):
        super().__init__(msg)


class FileFastaReader(QObject):

    __CANNOT_OPEN_FILE_ERROR: str = "Cannot open selected file"
    data_ready = Signal(str, str)

    def __init__(self):
        super().__init__()
        self._acceptableFilesRegex: QRegExp = QRegExp(".*.(fasta|txt)")

    def read(self, filePath: str) -> Sequence:
        if self.isValidFile(filePath):
            with open(filePath, "r", encoding="utf=8") as file:
                identifier = file.readline().strip()[1:].replace('"', '')
                identifierParts = identifier.split(" ")
                identifier = identifierParts[0]
                comment = " ".join(identifierParts[1:])
                sequence = "".join(file.readlines()).replace("\n", "")
                return Sequence(identifier, sequence, comment)
        else:
            return None

    def isValidFile(self, filePath):
        if QFile(filePath).exists():
            with open(filePath, "r", encoding="utf=8") as file:
                identifier = file.readline().strip()
                sequence = file.readline().strip()
                if len(identifier) > 0 and identifier[0] == ">" and sequence != "":
                    return True
        return False



