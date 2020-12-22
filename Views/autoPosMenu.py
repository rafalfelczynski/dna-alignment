from PySide2.QtWidgets import QMenu
from PySide2.QtGui import QShowEvent


class AutoPosMenu(QMenu):

    def __init__(self):
        super().__init__()

    def showEvent(self, event: QShowEvent) -> None:
        super().showEvent(event)
        geometry = self.geometry()
        height = geometry.height()
        geometry.setY(geometry.y() - geometry.height())
        geometry.setHeight(height)
        self.setGeometry(geometry)









