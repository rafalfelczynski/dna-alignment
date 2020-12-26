from PySide2.QtCore import *


class DragAndDropHandler(QObject):

    def __init__(self):
        super().__init__()

    def parseDroppedItems(self, draggedData: QMimeData):
        pass

    def exportDraggedItem(self, item: str, dragSourceIdentifier: QObject):
        pass





