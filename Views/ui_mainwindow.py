# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 500)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	border: 3px solid black;\n"
"	border-radius: 5px;\n"
"}")
        self.seqImportAction = QAction(MainWindow)
        self.seqImportAction.setObjectName(u"seqImportAction")
        self.helpAboutAction = QAction(MainWindow)
        self.helpAboutAction.setObjectName(u"helpAboutAction")
        self.scoringImportAction = QAction(MainWindow)
        self.scoringImportAction.setObjectName(u"scoringImportAction")
        self.resultsImportAction = QAction(MainWindow)
        self.resultsImportAction.setObjectName(u"resultsImportAction")
        self.resultsShowAction = QAction(MainWindow)
        self.resultsShowAction.setObjectName(u"resultsShowAction")
        self.seqFromNetAction = QAction(MainWindow)
        self.seqFromNetAction.setObjectName(u"seqFromNetAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: #333333;\n"
"	font: \"Times New Roman\";\n"
"    font-size: 14px;\n"
"}\n"
"QLabel {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"	font: italic \"Times New Roman\";\n"
"}\n"
"QLineEdit {\n"
"	border-radius: 8px;\n"
"	border: 1px solid white;\n"
"	background-color: #999999;\n"
"	color: white;\n"
"}\n"
"QGroupBox {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}\n"
"QRadioButton {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"    border: 2px outset white;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1,\n"
"    stop: 0 white,\n"
"    stop: 0.3 gray,\n"
"    stop: 0.6 gray,\n"
"    stop: 0.9 darkgray,\n"
"    stop: 1 black);\n"
"    font-size: 14px;\n"
"	font: bold \"Times New Roman\";\n"
"	height: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1,\n"
"    stop: 0 black,\n"
"    stop: "
                        "0.3 darkgray,\n"
"    stop: 0.6 gray,\n"
"    stop: 0.8 gray,\n"
"    stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 4px solid green;\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_10 = QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.gridLayout_11 = QGridLayout(self.groupBox_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 9, -1, -1)
        self.activeProcTableWidget = QTableWidget(self.groupBox_10)
        if (self.activeProcTableWidget.columnCount() < 10):
            self.activeProcTableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.activeProcTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.activeProcTableWidget.setObjectName(u"activeProcTableWidget")
        self.activeProcTableWidget.setStyleSheet(u"QTableWidget {\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	color: white;\n"
"	selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}")
        self.activeProcTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.activeProcTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.activeProcTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.activeProcTableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.activeProcTableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.activeProcTableWidget.verticalHeader().setVisible(False)

        self.gridLayout_11.addWidget(self.activeProcTableWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_10, 2, 2, 1, 6)

        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.seqSecLedLbl = QLabel(self.groupBox_8)
        self.seqSecLedLbl.setObjectName(u"seqSecLedLbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.seqSecLedLbl.sizePolicy().hasHeightForWidth())
        self.seqSecLedLbl.setSizePolicy(sizePolicy2)
        self.seqSecLedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"	border: 3px solid black;\n"
"	background-color: rgba(255, 173, 51, 200);;\n"
"	color: black;\n"
"}")
        self.seqSecLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.seqSecLedLbl, 5, 0, 2, 1)

        self.scoringLedLbl = QLabel(self.groupBox_8)
        self.scoringLedLbl.setObjectName(u"scoringLedLbl")
        sizePolicy2.setHeightForWidth(self.scoringLedLbl.sizePolicy().hasHeightForWidth())
        self.scoringLedLbl.setSizePolicy(sizePolicy2)
        self.scoringLedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"	border: 3px solid black;\n"
"	background-color: rgba(255, 173, 51, 200);\n"
"	color: black;\n"
"}")
        self.scoringLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.scoringLedLbl, 7, 0, 2, 1)

        self.seqFirstLedLbl = QLabel(self.groupBox_8)
        self.seqFirstLedLbl.setObjectName(u"seqFirstLedLbl")
        sizePolicy2.setHeightForWidth(self.seqFirstLedLbl.sizePolicy().hasHeightForWidth())
        self.seqFirstLedLbl.setSizePolicy(sizePolicy2)
        self.seqFirstLedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"	border: 3px solid black;\n"
"	background-color: rgba(255, 173, 51, 200);\n"
"	color: black;\n"
"}\n"
"")
        self.seqFirstLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.seqFirstLedLbl, 3, 0, 2, 1)

        self.processBtn = QPushButton(self.groupBox_8)
        self.processBtn.setObjectName(u"processBtn")
        sizePolicy2.setHeightForWidth(self.processBtn.sizePolicy().hasHeightForWidth())
        self.processBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.processBtn, 7, 1, 2, 1)

        self.operationGroupBox = QGroupBox(self.groupBox_8)
        self.operationGroupBox.setObjectName(u"operationGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.operationGroupBox.sizePolicy().hasHeightForWidth())
        self.operationGroupBox.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.operationGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dotplotRadioBtn = QRadioButton(self.operationGroupBox)
        self.dotplotRadioBtn.setObjectName(u"dotplotRadioBtn")
        sizePolicy1.setHeightForWidth(self.dotplotRadioBtn.sizePolicy().hasHeightForWidth())
        self.dotplotRadioBtn.setSizePolicy(sizePolicy1)
        self.dotplotRadioBtn.setChecked(True)

        self.verticalLayout_2.addWidget(self.dotplotRadioBtn)

        self.alignmentRadioBtn = QRadioButton(self.operationGroupBox)
        self.alignmentRadioBtn.setObjectName(u"alignmentRadioBtn")
        sizePolicy1.setHeightForWidth(self.alignmentRadioBtn.sizePolicy().hasHeightForWidth())
        self.alignmentRadioBtn.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.alignmentRadioBtn)


        self.gridLayout_9.addWidget(self.operationGroupBox, 3, 1, 4, 1)


        self.gridLayout_6.addWidget(self.groupBox_8, 1, 7, 1, 1)

        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy1.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy1)
        self.groupBox_9.setMinimumSize(QSize(100, 20))
        self.groupBox_9.setSizeIncrement(QSize(1, 0))
        self.groupBox_9.setBaseSize(QSize(80, 0))
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_10 = QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(5, -1, 5, 9)
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.matchLineEdit = QLineEdit(self.groupBox_9)
        self.matchLineEdit.setObjectName(u"matchLineEdit")
        sizePolicy2.setHeightForWidth(self.matchLineEdit.sizePolicy().hasHeightForWidth())
        self.matchLineEdit.setSizePolicy(sizePolicy2)
        self.matchLineEdit.setMinimumSize(QSize(50, 0))
        self.matchLineEdit.setAlignment(Qt.AlignCenter)
        self.matchLineEdit.setClearButtonEnabled(False)

        self.gridLayout_10.addWidget(self.matchLineEdit, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_9)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(80, 0))

        self.gridLayout_10.addWidget(self.label_8, 1, 0, 1, 1)

        self.mismatchLineEdit = QLineEdit(self.groupBox_9)
        self.mismatchLineEdit.setObjectName(u"mismatchLineEdit")
        sizePolicy2.setHeightForWidth(self.mismatchLineEdit.sizePolicy().hasHeightForWidth())
        self.mismatchLineEdit.setSizePolicy(sizePolicy2)
        self.mismatchLineEdit.setMinimumSize(QSize(50, 0))
        self.mismatchLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.mismatchLineEdit, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.label_9, 2, 0, 1, 1)

        self.gapLineEdit = QLineEdit(self.groupBox_9)
        self.gapLineEdit.setObjectName(u"gapLineEdit")
        sizePolicy2.setHeightForWidth(self.gapLineEdit.sizePolicy().hasHeightForWidth())
        self.gapLineEdit.setSizePolicy(sizePolicy2)
        self.gapLineEdit.setMinimumSize(QSize(50, 0))
        self.gapLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.gapLineEdit, 2, 1, 1, 1)

        self.fetchScoringBtn = QPushButton(self.groupBox_9)
        self.fetchScoringBtn.setObjectName(u"fetchScoringBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fetchScoringBtn.sizePolicy().hasHeightForWidth())
        self.fetchScoringBtn.setSizePolicy(sizePolicy5)

        self.gridLayout_10.addWidget(self.fetchScoringBtn, 3, 0, 1, 2)


        self.gridLayout_6.addWidget(self.groupBox_9, 1, 6, 1, 1)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QSize(50, 0))
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.selectSeqSecBtn = QPushButton(self.groupBox_7)
        self.selectSeqSecBtn.setObjectName(u"selectSeqSecBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.selectSeqSecBtn.sizePolicy().hasHeightForWidth())
        self.selectSeqSecBtn.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.selectSeqSecBtn, 2, 2, 1, 1)

        self.seq1ListWidget = QListWidget(self.groupBox_7)
        self.seq1ListWidget.setObjectName(u"seq1ListWidget")
        sizePolicy.setHeightForWidth(self.seq1ListWidget.sizePolicy().hasHeightForWidth())
        self.seq1ListWidget.setSizePolicy(sizePolicy)
        self.seq1ListWidget.setStyleSheet(u"QListView::item {\n"
"	color: white;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}")
        self.seq1ListWidget.setProperty("isWrapping", False)
        self.seq1ListWidget.setWordWrap(True)

        self.gridLayout.addWidget(self.seq1ListWidget, 1, 1, 1, 1)

        self.selectSeqFirstBtn = QPushButton(self.groupBox_7)
        self.selectSeqFirstBtn.setObjectName(u"selectSeqFirstBtn")
        sizePolicy7.setHeightForWidth(self.selectSeqFirstBtn.sizePolicy().hasHeightForWidth())
        self.selectSeqFirstBtn.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.selectSeqFirstBtn, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.seq2ListWidget = QListWidget(self.groupBox_7)
        self.seq2ListWidget.setObjectName(u"seq2ListWidget")
        self.seq2ListWidget.setStyleSheet(u"QListView::item {\n"
"	color: white;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}")
        self.seq2ListWidget.setProperty("isWrapping", False)
        self.seq2ListWidget.setWordWrap(True)

        self.gridLayout.addWidget(self.seq2ListWidget, 1, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_7, 1, 2, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSequence = QMenu(self.menubar)
        self.menuSequence.setObjectName(u"menuSequence")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuResults = QMenu(self.menubar)
        self.menuResults.setObjectName(u"menuResults")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSequence.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.scoringImportAction)
        self.menuSequence.addAction(self.seqImportAction)
        self.menuSequence.addAction(self.seqFromNetAction)
        self.menuHelp.addAction(self.helpAboutAction)
        self.menuResults.addAction(self.resultsImportAction)
        self.menuResults.addAction(self.resultsShowAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.seqImportAction.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.helpAboutAction.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.scoringImportAction.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.resultsImportAction.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.resultsShowAction.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.seqFromNetAction.setText(QCoreApplication.translate("MainWindow", u"Get from the Internet", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Active processes", None))
        ___qtablewidgetitem = self.activeProcTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.activeProcTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem2 = self.activeProcTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.activeProcTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Seq1", None));
        ___qtablewidgetitem4 = self.activeProcTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Seq2", None));
        ___qtablewidgetitem5 = self.activeProcTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Match", None));
        ___qtablewidgetitem6 = self.activeProcTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Mismatch", None));
        ___qtablewidgetitem7 = self.activeProcTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Gap", None));
        ___qtablewidgetitem8 = self.activeProcTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"%CPU", None));
        ___qtablewidgetitem9 = self.activeProcTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"%MEM", None));
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.seqSecLedLbl.setText(QCoreApplication.translate("MainWindow", u"Seq2", None))
        self.scoringLedLbl.setText(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.seqFirstLedLbl.setText(QCoreApplication.translate("MainWindow", u"Seq1", None))
        self.processBtn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.operationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.dotplotRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Dotplot", None))
        self.alignmentRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mismatch", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gap", None))
        self.fetchScoringBtn.setText(QCoreApplication.translate("MainWindow", u"Fetch scoring", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sequence 2", None))
        self.selectSeqSecBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.selectSeqFirstBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sequence 1", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.menuSequence.setTitle(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuResults.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
    # retranslateUi

