from PySide2.QtWidgets import QListWidget
from PySide2.QtGui import *
from PySide2.QtCore import Signal, QMimeData, QObject


class Identifier(QObject):

    def __init__(self, id: int):
        super().__init__()
        self.identifier = id

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __ne__(self, other):
        return not self == other


class DragNDropListWidget(QListWidget):
    __START_DRAG_DISTANCE = 30
    __DRAG_SOURCE_IDENTIFIER: QObject = Identifier(1)
    item_dragged = Signal(str, QObject)
    item_dropped = Signal(QMimeData)
    item_double_clicked = Signal(str)
    item_right_clicked = Signal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self._dragStartPos: QPoint = ...

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._dragStartPos = event.pos()
        if event.button() == Qt.MouseButton.RightButton:
            item = self.itemAt(event.pos())
            if item is not None:
                seqId = item.text()
                self.item_right_clicked.emit(seqId)
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        seqId = self.currentItem().text()
        if seqId:
            self.item_double_clicked.emit(seqId)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.source() is None or (event.source() != DragNDropListWidget.__DRAG_SOURCE_IDENTIFIER):
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        pass
        # self.dndHandler.dragMoveEvent(event, self)

    def dropEvent(self, event: QDropEvent) -> None:
        self.item_dropped.emit(event.mimeData())

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if Qt.MouseButton.LeftButton == event.buttons():
            if (event.pos() - self._dragStartPos).manhattanLength() > self.__START_DRAG_DISTANCE:
                item = self.convertDraggedItemToString()
                if item:
                    self.item_dragged.emit(item, DragNDropListWidget.__DRAG_SOURCE_IDENTIFIER)

    def convertDraggedItemToString(self) -> str:
        item = self.itemAt(self._dragStartPos)
        if item is not None:
            return item.text()
        else:
            return ""














