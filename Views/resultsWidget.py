from typing import List

from Models.alignment import Alignment
from Models.dotplot import Dotplot
from Views.ui_results import *


class ResultsWidget(QWidget):

    dotplots_requested = Signal()
    alignments_requested = Signal()
    dotplot_selected = Signal(Dotplot)
    alignment_selected = Signal(Alignment)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ResultsWidget()
        self.ui.setupUi(self)
        self.ui.dotpTableWidget.dotplot_double_clicked.connect(self.dotplot_selected)
        self.ui.alignTableWidget.alignment_double_clicked.connect(self.alignment_selected)

    def showEvent(self, event: QShowEvent) -> None:
        self.dotplots_requested.emit()
        self.alignments_requested.emit()

    def refreshDotplots(self, dotplots: List[Dotplot]) -> None:
        self.ui.dotpTableWidget.refreshData(dotplots)

    def refreshAlignments(self, aligns: List[Alignment]) -> None:
        self.ui.alignTableWidget.refreshData(aligns)





