from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QMimeData
from PySide2.QtGui import QDragEnterEvent, QDropEvent


class DragNDropWidget(QWidget):

    drag_and_drop_accepted = Signal(QMimeData)

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        print("drag and drop widget drag enter")
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        print("drop event")
        self.drag_and_drop_accepted.emit(event.mimeData())









