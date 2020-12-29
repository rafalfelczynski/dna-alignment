from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Views.resultsWidget import ResultsWidget
from Models.Database.dotplotReader import DotplotReader
from Models.Database.alignmentReader import AlignmentReader
from Views.dotplotChart import DotplotChart
from Models.dotplot import Dotplot
from Models.alignment import Alignment


class ResultsController(QObject):

    def __init__(self, resultsWidget, dotplotReader, alignReader):
        super().__init__()
        self._resultsWidget: ResultsWidget = resultsWidget
        self._dotplotReader: DotplotReader = dotplotReader
        self._alignReader: AlignmentReader = alignReader
        self._connectWidget()
        self._tabs = dict()

    def _connectWidget(self):
        self._resultsWidget.dotplots_requested.connect(self._refreshDotplots)
        self._resultsWidget.dotplot_selected.connect(self.showDotplot)
        self._resultsWidget.alignments_requested.connect(self._refreshAlignments)
        self._resultsWidget.alignment_selected.connect(self.showAlignment)

    def _refreshDotplots(self):
        dotplots = self._dotplotReader.readAllDotplots()
        self._resultsWidget.refreshDotplots(dotplots)

    def _refreshAlignments(self):
        aligns = self._alignReader.readAllAlignments()
        self._resultsWidget.refreshAlignments(aligns)

    def showDotplot(self, dotp):
        if not self.dotplotAlreadyOpen(dotp):
            dotplot = self._dotplotReader.readDotplot(dotp.seq1.identifier, dotp.seq2.identifier)
            if dotplot.isValid():
                self.openDotplotWindow(dotplot)
        else:
            tab = self._tabs[(dotp.seq1.identifier, dotp.seq2.identifier)]
            tab.showNormal()
            tab.setFocus()

    def openDotplotWindow(self, dotp):
        # Create dotplot in tab
        tab = DotplotChart()
        tab.widget_closed.connect(self.dotplotTabClosed)
        self._tabs[(dotp.seq1.identifier, dotp.seq2.identifier)] = tab
        tab.setDotplot(dotp)
        tab.resize(640, 480)
        tab.show()

    def dotplotAlreadyOpen(self, dotp):
        if (dotp.seq1.identifier, dotp.seq2.identifier) in self._tabs:
            return True
        return False

    def dotplotTabClosed(self, ids):
        self._tabs.pop(ids)

    def showAlignment(self, align):
        alignment = self._alignReader.readAlignment(align.seq1.identifier, align.seq2.identifier, align.scoring)
        if alignment.isValid():
            self._resultsWidget.showAlignment(alignment)

    def showAlignmentWindow(self, align: Alignment):
        pass






