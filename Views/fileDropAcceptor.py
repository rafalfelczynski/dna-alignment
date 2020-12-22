from PySide2.QtWidgets import *
from PySide2.QtGui import *
import PySide2.QtGui
from PySide2.QtCore import *
import resources.res


class FileDropAcceptor(QWidget):
    __START_DRAG_DISTANCE = 20

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self._pixmap = QPixmap(":/dna_icon.png").scaled(50, 50,
                                                        Qt.AspectRatioMode.IgnoreAspectRatio,
                                                        Qt.TransformationMode.SmoothTransformation)
        self._dragStartPos = QPoint(0, 0)
        self._fastaFileRegex = QRegExp(".*.(fasta|txt)", Qt.CaseInsensitive)

    # def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
    #     print("startDrag:", QApplication.startDragDistance())
    #     if event.button() == PySide2.QtGui.Qt.LeftButton:
    #         self._dragStartPos = event.pos()
    #
    # def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
    #     if (event.pos() - self._dragStartPos).manhattanLength() > self.__START_DRAG_DISTANCE:
    #         print("drag")
    #         drag = QDrag(self)
    #         mimeData = QMimeData()
    #         mimeData.setText("Pliczek")
    #         drag.setMimeData(mimeData)
    #         drag.setPixmap(self._pixmap)
    #         dropAction = drag.exec_()

    def dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None:
        draggedData = event.mimeData()
        if draggedData.hasUrls():
            fileNames = draggedData.text().splitlines()
            shouldAccept = True
            for fileName in fileNames:
                if not self._fastaFileRegex.exactMatch(fileName):
                    shouldAccept = False
            if shouldAccept:
                event.acceptProposedAction()

    def dragMoveEvent(self, event: PySide2.QtGui.QDragMoveEvent) -> None:
        # print("dragging")
        ...

    def dragLeaveEvent(self, event: PySide2.QtGui.QDragLeaveEvent) -> None:
        print("drag left")

    def dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None:
        draggedData = event.mimeData()
        fileNames = draggedData.text().splitlines()
        regex = QRegExp("file:///(.*.(fasta|txt))")
        for name in fileNames:
            if regex.exactMatch(name):
                name = regex.cap(1)
                with open(name, "r", encoding="utf=8") as file:
                    identifier = file.readline().strip()
                    if len(identifier) > 0 and identifier[0] == ">":
                        identifier = identifier[1:]
                        sequence = "".join(file.readlines()).replace("\n", "")
                        print("id:", identifier)
                        print("seq:", sequence)

