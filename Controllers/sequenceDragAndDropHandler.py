from PySide2.QtGui import *

from Controllers.dndFileParser import DnDFileParser
from Controllers.dndHandler import *
from Views.infoDialog import InfoDialog
from Models.Database.sequenceRepository import SequenceRepository


class SequenceDragAndDropHandler(DragAndDropHandler):

    def __init__(self, relatedWidget, seqRepo : SequenceRepository):
        super().__init__()
        self.relatedWidget = relatedWidget
        self._seqRepo = seqRepo
        self.fileParser = DnDFileParser()

    def parseDroppedItems(self, draggedData: QMimeData):
        sequences, acceptedFiles, rejectedFiles = self.fileParser.parseDraggedItems(draggedData)
        addedSequences = []
        rejectedSequences = []
        for seq in sequences:
            wasAdded = self._seqRepo.writeSeq(seq)
            if wasAdded:
                addedSequences.append(seq.identifier)
                self.relatedWidget.newSeqAvailable(seq.identifier)
            else:
                rejectedSequences.append(seq.identifier)
        if len(rejectedFiles) > 0 or len(rejectedSequences) > 0:
            self._showAccRejFilesAndSeqs(acceptedFiles, rejectedFiles, addedSequences, rejectedSequences)

    def exportDraggedItem(self, item: str, sourceIdentifier: QObject):
        seq = self._seqRepo.readSeq(item)
        if seq.isNotEmpty():
            drag = QDrag(sourceIdentifier)
            mimeData = QMimeData()
            cwd = QDir.current()
            cwd.mkdir("temp")
            file = QFile(f"temp/{seq.identifier}.fasta")
            fileInfo = QFileInfo(file)
            file.open(QFile.WriteOnly)
            file.write(QByteArray(f">{seq.identifier} {seq.comment}\n{seq.cutSequenceIntoFragments(80)}".encode("utf-8")))
            file.close()
            url = QUrl.fromLocalFile(fileInfo.absoluteFilePath())
            mimeData.setUrls([url])
            drag.setMimeData(mimeData)
            dragIcon: QPixmap = QPixmap(":/notepad_icon.png").scaled(50, 50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            drag.setPixmap(dragIcon)
            drag.exec_(Qt.CopyAction, Qt.CopyAction)
            file.remove()

    def _showAccRejFilesAndSeqs(self, acceptedFiles, rejectedFiles, acceptedSeqs, rejectedSeqs):
        infoText = ""
        infoText += f"Accepted files:\n{self._elementsToText(acceptedFiles)}"
        infoText += f"\n\nRejected files:\n{self._elementsToText(rejectedFiles)}"
        infoText += f"\n\nNew sequences:\n{self._elementsToText(acceptedSeqs)}"
        infoText += f"\n\nAlready existing sequences:\n{self._elementsToText(rejectedSeqs)}"
        dialog = InfoDialog()
        dialog.resize(400, 250)
        dialog.setText(infoText)
        dialog.exec_()

    def _elementsToText(self, elements):
        if len(elements) > 0:
            index = 1
            text = ""
            for el in elements:
                text += f" {index}. {el}\n"
                index += 1
            return text
        else:
            return "Nothing"







