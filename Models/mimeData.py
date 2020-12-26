from PySide2.QtCore import *
import typing


class MimeData(QMimeData):

    def __init__(self):
        super().__init__()

    def retrieveData(self, mimetype:str, preferredType:type) -> typing.Any:
        file = QFile("aaa.fasta")
        file.write(QByteArray(b"abcdef"))
        file.close()
        return "file:///aaa.fasta"






