from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Models.dotplot import Dotplot
import PyQt5
from QCustomPlot2 import *


class DotplotChart(QCustomPlot):

    __MARKER_SIZE = 3
    __BACKGROUND_COLOR: QColor = QColor(0, 0, 0, 255)
    widget_closed = pyqtSignal(tuple)
    screenshot_requested = pyqtSignal(QCustomPlot)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dotp = ...
        self.setAntialiasedElements(QCP.AntialiasedElement.aeAll)
        self.setBackground(QBrush(Qt.NoBrush))
        self._setAxesAttributes()
        self.setInteractions(QCP.Interactions(QCP.iRangeDrag | QCP.iRangeZoom))

    def paintEvent(self, event: QPaintEvent) -> None:
        self._drawRect(0, 0, self.width(), self.height())
        super().paintEvent(event)

    def closeEvent(self, event: QCloseEvent):
        self.widget_closed.emit((self.dotp.seq1.identifier, self.dotp.seq2.identifier))

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Space:
            self.screenshot_requested.emit(self)

    def _drawRect(self, x, y, w, h):
        painter = QPainter(self)
        painter.setBrush(DotplotChart.__BACKGROUND_COLOR)
        painter.drawRect(x, y, w, h)
        painter.end()

    def setDotplot(self, dotp: Dotplot):
        self.dotp = dotp
        self.clearGraphs()
        graph = self.addGraph()
        xs, ys = dotp.mapToXY()
        graph.setData(xs, ys)
        graph.setLineStyle(QCPGraph.LineStyle.lsNone)
        graph.setScatterStyle(QCPScatterStyle(QCPScatterStyle.ScatterShape.ssDisc, DotplotChart.__MARKER_SIZE))
        self.yAxis.setLabel(dotp.seq1.identifier)
        self.xAxis.setLabel(dotp.seq2.identifier)
        self.rescaleAxes()

    def _setAxesAttributes(self):
        color = QColor(255, 255, 255, 255)
        self.yAxis.setLabel("SEQUENCE 1")
        self.yAxis.setLabelColor(color)
        self.xAxis.setLabel("SEQUENCE 2")
        self.xAxis.setLabelColor(color)
        font = QFont("Arial", 15, 2, True)
        font.setPixelSize(15)
        self.yAxis.setLabelFont(font)
        self.xAxis.setLabelFont(font)
        self.xAxis.setTickLabelColor(color)
        pen = QPen()
        pen.setColor(color)
        self.yAxis.setBasePen(pen)
        self.xAxis.setBasePen(pen)
        self.yAxis.setTickPen(pen)
        self.xAxis.setTickPen(pen)
        self.yAxis.setTickLabelColor(color)
        self.xAxis.setTickLabelColor(color)
        self.yAxis.grid().setVisible(False)
        self.xAxis.grid().setVisible(False)
        self.yAxis.setVisible(True)
        self.xAxis.setVisible(True)




