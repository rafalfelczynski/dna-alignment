from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtNetwork import *


class InternetConnectionChecker(QObject):
    __CHECKING_INTERVAL = 3000
    connection_ok = Signal()
    no_connection = Signal()

    def __init__(self, networkManager: QNetworkAccessManager):
        super().__init__()
        self._netMan = networkManager
        self._timer: QTimer = QTimer()
        self._isChecking = False
        self._timerConnection: QMetaObject.Connection = ...
        self.connectionGraphics: QLabel = QLabel()
        self._connectionStatus = True

    def setConnectionGraphicsView(self, view):
        self.connectionGraphics = view
        QTimer.singleShot(50, lambda: self.setOkConnPixmap())

    def startChecking(self):
        self._isChecking = True
        self._timer.timeout.connect(self._checkConnection)
        self._timer.start(InternetConnectionChecker.__CHECKING_INTERVAL)

    def isConnectionWorking(self):
        return self._connectionStatus

    def stopChecking(self):
        self._isChecking = False
        self._timer.stop()
        self._timer.timeout.disconnect(self._checkConnection)

    def _checkConnection(self):
        reply = self._netMan.get(QNetworkRequest(QUrl("https://google.com")))
        reply.finished.connect(lambda: self._parseReply(reply))
        reply.errorOccurred.connect(self._notifyNoConnection)

    def _parseReply(self, reply: QNetworkReply):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            self._notifyConnectionOk()
        else:
            self._notifyNoConnection()

    def setOkConnPixmap(self):
        self.connectionGraphics.setPixmap(QPixmap(":/connection_ok.png").scaled(self.connectionGraphics.size(),
                                          Qt.AspectRatioMode.IgnoreAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation))

    def setNoConnPixmap(self):
        self.connectionGraphics.setPixmap(QPixmap(":/no_connection.png").scaled(self.connectionGraphics.size(),
                                          Qt.AspectRatioMode.IgnoreAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation))

    def _notifyNoConnection(self):
        self.setNoConnPixmap()
        self._connectionStatus = False
        self.no_connection.emit()

    def _notifyConnectionOk(self):
        self.setOkConnPixmap()
        self._connectionStatus = True
        self.connection_ok.emit()
