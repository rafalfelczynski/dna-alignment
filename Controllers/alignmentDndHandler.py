from Controllers.dndHandler import *
from PySide2.QtGui import *
from PySide2.QtCore import Signal
from Controllers.dndFileParser import DnDFileParser
from Views.infoDialog import InfoDialog
from Models.scoring import Scoring
from Models.Database.alignmentRepository import AlignmentRepository


class AlignmentDndHandler(DragAndDropHandler):

    def __init__(self, alignRepo: AlignmentRepository):
        super().__init__()
        self._alignRepo = alignRepo
        self.fileParser = DnDFileParser()

    def parseDroppedItems(self, draggedData: QMimeData):
        raise NotImplementedError("Dropping items is not supported")

    def exportDraggedItem(self, item: str, sourceIdentifier: QObject):
        ids = item.split("$$$")
        scoring = Scoring(float(ids[2]), float(ids[3]), float(ids[4]))
        align = self._alignRepo.readAlignment(ids[0], ids[1], scoring)
        if align.isValid():
            drag = QDrag(sourceIdentifier)
            mimeData = QMimeData()
            file = QFile(f"temp/{align.seq1.identifier}_{align.seq2.identifier}_{align.scoring.match}_{align.scoring.mismatch}_{align.scoring.gap}.txt")
            fileInfo = QFileInfo(file)
            file.open(QFile.WriteOnly)
            file.write(QByteArray(f"{align.info()}\n".encode("utf-8")))
            file.close()
            url = QUrl.fromLocalFile(fileInfo.absoluteFilePath())
            mimeData.setUrls([url])
            drag.setMimeData(mimeData)
            dragIcon: QPixmap = QPixmap(":/alignment.png").scaled(50, 50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            drag.setPixmap(dragIcon)
            drag.exec_(Qt.CopyAction, Qt.CopyAction)
            file.remove()







