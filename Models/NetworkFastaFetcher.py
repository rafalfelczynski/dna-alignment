from PySide2.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager, QSslError, QSslSocket, QSslConfiguration
from PySide2.QtCore import QUrl, QUrlQuery, Signal, QObject


class NetworkFastaFetcher(QObject):
    __DATABASE_ENDPOINT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    __ERROR_CODES_MSGS = {
        QNetworkReply.NetworkError.TimeoutError: "*** Timeout error *** Check your Internet Connection!",
        QNetworkReply.NetworkError.ConnectionRefusedError: "*** Connection Refused *** "
                                                           "The server is currently not accepting requests."
                                                           " Try again later!",
        QNetworkReply.NetworkError.NoError: "Everything was OK."
    }
    __UNKNOWN_ERROR_MSG = "UNKNOWN ERROR"
    data_ready = Signal(str, str)
    error_occurred = Signal(str)

    def __init__(self, networkManager: QNetworkAccessManager):
        super().__init__()
        self.__replyObjects = {}
        self.__networkManager = networkManager
        self.__replyCounter = 0

    def fetchFasta(self, identifier: str):
        query = QUrlQuery()
        query.addQueryItem("db", "nucleotide")
        query.addQueryItem("rettype", "fasta")
        query.addQueryItem("id", str(identifier))
        url = QUrl(self.__DATABASE_ENDPOINT)
        url.setQuery(query.query())
        request = QNetworkRequest(url)
        replyObj = self.__networkManager.get(request)
        replyObj.finished.connect(lambda: self.__dataFetched(self.__replyCounter))
        replyObj.setSslConfiguration(QSslConfiguration.defaultDtlsConfiguration())
        replyObj.sslErrors.connect(self._sslErrorsOccurred)
        replyObj.errorOccurred.connect(lambda code: self._parseError(code, identifier, replyObj))
        self.__replyObjects[self.__replyCounter] = replyObj

    def __dataFetched(self, replyObjId):
        if replyObjId in self.__replyObjects:
            reply = self.__replyObjects[replyObjId]
            identifier = ""
            sequence = ""
            if reply.isFinished():
                identifier = reply.readLine().data().decode().replace("\n", "")
                sequence = reply.readAll().data().decode().replace("\n", "")
                identifier, sequence = self.__validateFetchedData(identifier, sequence)
            self.data_ready.emit(identifier, sequence)
            self.__replyObjects.pop(replyObjId)
        else:
            self.error_occurred.emit(f"Reply object id {replyObjId} not known!")

    def _parseError(self, errorCode: QNetworkReply.NetworkError, identifier, reply):
        if errorCode in self.__ERROR_CODES_MSGS:
            self.error_occurred.emit(f"There was an error{self.__ERROR_CODES_MSGS[errorCode]} during"
                                     f" processing of request for identifier: {identifier}")
        else:
            self.error_occurred.emit(f"There was an error {self.__UNKNOWN_ERROR_MSG} during"
                                     f" processing of request for identifier: {identifier}"
                                     f" Error message: {reply.errorString()}")

    def _sslErrorsOccurred(self, errors):
        print("ssl errors")
        for err in errors:  # type: QSslError
            self.error_occurred.emit("SSL error! " + err.errorString())

    def __validateFetchedData(self, identifier: str, sequence: str):
        if len(identifier) > 0 and identifier[0] == '>':
            return identifier[1:], sequence
        else:
            if "Error" in identifier:
                self.error_occurred.emit(f"Error occurred: {identifier}")
            return "", ""
