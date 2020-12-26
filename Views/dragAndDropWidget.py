

class DragAndDropWidget:

    __START_DRAG_DISTANCE = 30
    item_dragged = Signal(str)
    item_dropped = Signal(QMimeData)

    def __init__(self, widget: QWidget):
        super().__init__()
        print("drag n drop widget konstruktor")
        self.widget = widget
        self.widget.setAcceptDrops(True)
        self._dragStartPos: QPoint = ...

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print("press")
        if event.button() == Qt.MouseButton.LeftButton:
            self._dragStartPos = event.pos()
        QWidget.mousePressEvent(self.widget, event)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        self.item_dropped.emit(event.mimeData())

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if Qt.MouseButton.LeftButton == event.buttons():
            if (event.pos() - self._dragStartPos).manhattanLength() > self.__START_DRAG_DISTANCE:
                item = self.widget.convertDraggedItemToString()
                if item:
                    self.item_dragged.emit(item)






