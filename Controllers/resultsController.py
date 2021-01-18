import PyQt5
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
from PySide2.QtCore import *

from Controllers.dndHandler import DragAndDropHandler
from Models.Database.dotplotRepository import DotplotRepository
from Models.Database.alignmentRepository import AlignmentRepository
from Models.alignment import Alignment
from Models.scoring import Scoring
from Views.confirmDialog import ConfirmDialog
from Views.dotplotChart import DotplotChart
from Views.infoDialog import InfoDialog
from Views.insertTextDialog import InsertTextDialog
from Views.resultsWidget import ResultsWidget


class ResultsController(QObject):

    __SCREENSHOT_LOCATION = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    __SCREENSHOT_FOLDER = "alignment"

    screenshot_saved = Signal(str, str)

    def __init__(self, resultsWidget, dotpRepo: DotplotRepository, alignRepo: AlignmentRepository,
                 dndHandler: DragAndDropHandler):
        super().__init__()
        self._resultsWidget: ResultsWidget = resultsWidget
        self._dotplotRepo = dotpRepo
        self._alignRepo = alignRepo
        self._dndHandler = dndHandler
        self._connectWidget()
        self._resultWindows = dict()

    def _connectWidget(self):
        self._resultsWidget.dotplots_requested.connect(self._refreshDotplots)
        self._resultsWidget.dotplot_selected.connect(self.showDotplot)
        self._resultsWidget.alignments_requested.connect(self._refreshAlignments)
        self._resultsWidget.alignment_selected.connect(self.showAlignment)
        self._resultsWidget.ui.alignTableWidget.item_dragged.connect(self._dndHandler.exportDraggedItem)
        self._resultsWidget.ui.dotpTableWidget.item_right_clicked.connect(self._removeDotplotConfirm)
        self._resultsWidget.ui.alignTableWidget.item_right_clicked.connect(self._removeAlignmentConfirm)

    def _refreshDotplots(self):
        dotplots = self._dotplotRepo.listAllDotplots()
        self._resultsWidget.refreshDotplots(dotplots)

    def _refreshAlignments(self):
        aligns = self._alignRepo.readAllAlignments()
        self._resultsWidget.refreshAlignments(aligns)

    def _removeDotplotConfirm(self, idAsString):
        ids = idAsString.split("$$$")
        dialog = ConfirmDialog()
        dialog.setText(f"Are you sure you want to remove this dotplot?\n"
                       f"Sequence 1 Id: {ids[0]}\n"
                       f"Sequence 2 Id: {ids[1]}")
        dialog.resize(400, 200)
        dialog.accepted.connect(lambda: self._removeDotplot(ids))
        dialog.exec_()

    def _removeDotplot(self, ids):
        self._dotplotRepo.deleteDotplot(ids[0], ids[1])
        self._refreshDotplots()

    def _removeAlignmentConfirm(self, idAsString):
        ids = idAsString.split("$$$")
        dialog = ConfirmDialog()
        dialog.setText(f"Are you sure you want to remove this dotplot?\n"
                       f"Sequence 1 Id: {ids[0]}\n"
                       f"Sequence 2 Id: {ids[1]}\n"
                       f"Match: {ids[2]}\n"
                       f"Mismatch: {ids[3]}\n"
                       f"Gap: {ids[4]}")
        dialog.resize(400, 200)
        dialog.accepted.connect(lambda: self._removeAlignment(ids))
        dialog.exec_()

    def _removeAlignment(self, ids):
        scoring = Scoring(float(ids[2]), float(ids[3]), float(ids[4]))
        self._alignRepo.deleteAlignment(ids[0], ids[1], scoring)
        self._refreshAlignments()

    def showDotplot(self, dotp):
        if not self.dotplotAlreadyOpen(dotp):
            dotplot = self._dotplotRepo.readDotplot(dotp.seq1.identifier, dotp.seq2.identifier)
            if dotplot.isValid():
                self.openDotplotWindow(dotplot)
        else:
            tab = self._resultWindows[(dotp.seq1.identifier, dotp.seq2.identifier)]
            tab.showNormal()
            tab.setFocus()

    def openDotplotWindow(self, dotp):
        tab = DotplotChart()
        tab.setWindowTitle("Dotplot")
        tab.screenshot_requested.connect(self._takeScreenshot)
        tab.widget_closed.connect(self.dotplotTabClosed)
        self._resultWindows[(dotp.seq1.identifier, dotp.seq2.identifier)] = tab
        tab.setDotplot(dotp)
        tab.resize(640, 480)
        tab.show()

    def dotplotAlreadyOpen(self, dotp):
        return (dotp.seq1.identifier, dotp.seq2.identifier) in self._resultWindows

    def dotplotTabClosed(self, ids):
        pass
        #self._resultWindows.pop(ids)

    def showAlignment(self, align):
        if not self.alignmentAlreadyOpen(align):
            alignment = self._alignRepo.readAlignment(align.seq1.identifier, align.seq2.identifier, align.scoring)
            if alignment.isValid():
                self.showAlignmentWindow(alignment)
        else:
            tab = self._resultWindows[align.ids()]
            tab.showNormal()
            tab.setFocus()

    def showAlignmentWindow(self, align: Alignment):
        dialog = InfoDialog()
        self._resultWindows[align.ids()] = dialog
        dialog.finished.connect(lambda: self.alignmentClosed(align))
        dialog.resize(800, 300)
        dialog.setText(align.cutInFragments(50))
        dialog.show()

    def alignmentAlreadyOpen(self, align):
        return align.ids() in self._resultWindows

    def alignmentClosed(self, align):
        self._resultWindows.pop(align.ids())

    def _takeScreenshot(self, window: PyQt5.QtWidgets.QWidget):
        try:
            self._ensureScreenshotFolderExists()
            image = PyQt5.QtGui.QImage(window.size(), PyQt5.QtGui.QImage.Format_ARGB32)
            painter = PyQt5.QtGui.QPainter(image)
            window.render(painter, PyQt5.QtCore.QPoint(0, 0), PyQt5.QtGui.QRegion(window.rect()), window.DrawChildren)
            dialog = InsertTextDialog()
            dialog.setEditFieldTitle("Type in file name (without extension)")
            dialog.setEditFieldText("screen")
            dialog.text_inserted.connect(lambda name: self._checkScreenshotLocation(name, image))
            dialog.exec_()
        except Exception:
            pass

    def _checkScreenshotLocation(self, name, image):
        directory = QDir(ResultsController.__SCREENSHOT_LOCATION)
        directory.cd(ResultsController.__SCREENSHOT_FOLDER)
        filePath = directory.absoluteFilePath(name + ".png")
        fileInfo = QFileInfo(filePath)
        if fileInfo.exists():
            confirmDialog = ConfirmDialog()
            confirmDialog.setText("File already exists. Do you want to overwrite it?")
            confirmDialog.resize(300, 150)
            confirmDialog.accepted.connect(lambda: self._saveScreenshot(filePath, image))
            confirmDialog.exec_()
        else:
            self._saveScreenshot(filePath, image)

    def _saveScreenshot(self, filePath, image):
        image.save(filePath)
        self.screenshot_saved.emit("Screenshot saved", "Screenshot saved succesfully!")

    def _ensureScreenshotFolderExists(self):
        directory = QDir(ResultsController.__SCREENSHOT_LOCATION)
        directory.mkdir(ResultsController.__SCREENSHOT_FOLDER)







