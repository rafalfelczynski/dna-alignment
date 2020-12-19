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
        MainWindow.resize(331, 427)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	border: 3px solid black;\n"
"	border-radius: 5px;\n"
"}")
        self.seqLoadFromFileAction = QAction(MainWindow)
        self.seqLoadFromFileAction.setObjectName(u"seqLoadFromFileAction")
        self.helpAboutAction = QAction(MainWindow)
        self.helpAboutAction.setObjectName(u"helpAboutAction")
        self.scoringLoadFromFileAction = QAction(MainWindow)
        self.scoringLoadFromFileAction.setObjectName(u"scoringLoadFromFileAction")
        self.resultsLoadFromFileAction = QAction(MainWindow)
        self.resultsLoadFromFileAction.setObjectName(u"resultsLoadFromFileAction")
        self.resultsShowAction = QAction(MainWindow)
        self.resultsShowAction.setObjectName(u"resultsShowAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
"    border: 2px solid white;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1,\n"
"    stop: 0 white,\n"
"    stop: 0.3 gray,\n"
"    stop: 0.6 gray,\n"
"    stop: 0.9 darkgray,\n"
"    stop: 1 black);\n"
"    font: bold \"Times New Roman\";\n"
"    font-size: 14px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1,\n"
"    stop: 0 black,\n"
"    stop"
                        ": 0.3 darkgray,\n"
"    stop: 0.6 gray,\n"
"    stop: 0.8 gray,\n"
"    stop: 1 white);\n"
"}\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.selectSeqFirstBtn = QPushButton(self.groupBox_7)
        self.selectSeqFirstBtn.setObjectName(u"selectSeqFirstBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectSeqFirstBtn.sizePolicy().hasHeightForWidth())
        self.selectSeqFirstBtn.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.selectSeqFirstBtn, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.seq2ListWidget = QListWidget(self.groupBox_7)
        self.seq2ListWidget.setObjectName(u"seq2ListWidget")

        self.gridLayout_8.addWidget(self.seq2ListWidget, 1, 1, 1, 1)

        self.seq1ListWidget = QListWidget(self.groupBox_7)
        self.seq1ListWidget.setObjectName(u"seq1ListWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.seq1ListWidget.sizePolicy().hasHeightForWidth())
        self.seq1ListWidget.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.seq1ListWidget, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 1, 1, 1)

        self.selectSeqSecBtn = QPushButton(self.groupBox_7)
        self.selectSeqSecBtn.setObjectName(u"selectSeqSecBtn")

        self.gridLayout_8.addWidget(self.selectSeqSecBtn, 3, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_7, 0, 4, 1, 1)

        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_10 = QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.matchLineEdit = QLineEdit(self.groupBox_9)
        self.matchLineEdit.setObjectName(u"matchLineEdit")
        self.matchLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.matchLineEdit, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_9)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_8, 1, 0, 1, 1)

        self.mismatchLineEdit = QLineEdit(self.groupBox_9)
        self.mismatchLineEdit.setObjectName(u"mismatchLineEdit")
        self.mismatchLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.mismatchLineEdit, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_9, 2, 0, 1, 1)

        self.gapLineEdit = QLineEdit(self.groupBox_9)
        self.gapLineEdit.setObjectName(u"gapLineEdit")
        self.gapLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.gapLineEdit, 2, 1, 1, 1)

        self.fetchScoringBtn = QPushButton(self.groupBox_9)
        self.fetchScoringBtn.setObjectName(u"fetchScoringBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fetchScoringBtn.sizePolicy().hasHeightForWidth())
        self.fetchScoringBtn.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.fetchScoringBtn, 3, 0, 1, 2)


        self.gridLayout_6.addWidget(self.groupBox_9, 0, 2, 1, 1)

        self.groupBox_10 = QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy2.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy2)
        self.groupBox_10.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.gridLayout_11 = QGridLayout(self.groupBox_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 9, -1, -1)
        self.activeProcListWidget = QListWidget(self.groupBox_10)
        self.activeProcListWidget.setObjectName(u"activeProcListWidget")

        self.gridLayout_11.addWidget(self.activeProcListWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_10, 1, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy2.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy2)
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.seq2LedLbl = QLabel(self.groupBox_8)
        self.seq2LedLbl.setObjectName(u"seq2LedLbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.seq2LedLbl.sizePolicy().hasHeightForWidth())
        self.seq2LedLbl.setSizePolicy(sizePolicy4)
        self.seq2LedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"	border: 3px solid black;\n"
"	background-color: #dd0000;\n"
"	color: black;\n"
"}")
        self.seq2LedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.seq2LedLbl, 4, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_8)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"	border: 3px solid black;\n"
"	background-color: #dd0000;\n"
"	color: black;\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_11, 5, 0, 1, 1)

        self.processBtn = QPushButton(self.groupBox_8)
        self.processBtn.setObjectName(u"processBtn")
        sizePolicy4.setHeightForWidth(self.processBtn.sizePolicy().hasHeightForWidth())
        self.processBtn.setSizePolicy(sizePolicy4)

        self.gridLayout_9.addWidget(self.processBtn, 5, 1, 1, 1)

        self.operationGroupBox = QGroupBox(self.groupBox_8)
        self.operationGroupBox.setObjectName(u"operationGroupBox")
        sizePolicy4.setHeightForWidth(self.operationGroupBox.sizePolicy().hasHeightForWidth())
        self.operationGroupBox.setSizePolicy(sizePolicy4)
        self.verticalLayout_2 = QVBoxLayout(self.operationGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dotplotRadioBtn = QRadioButton(self.operationGroupBox)
        self.dotplotRadioBtn.setObjectName(u"dotplotRadioBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dotplotRadioBtn.sizePolicy().hasHeightForWidth())
        self.dotplotRadioBtn.setSizePolicy(sizePolicy5)
        self.dotplotRadioBtn.setChecked(True)

        self.verticalLayout_2.addWidget(self.dotplotRadioBtn)

        self.alignmentRadioBtn = QRadioButton(self.operationGroupBox)
        self.alignmentRadioBtn.setObjectName(u"alignmentRadioBtn")
        sizePolicy5.setHeightForWidth(self.alignmentRadioBtn.sizePolicy().hasHeightForWidth())
        self.alignmentRadioBtn.setSizePolicy(sizePolicy5)

        self.verticalLayout_2.addWidget(self.alignmentRadioBtn)


        self.gridLayout_9.addWidget(self.operationGroupBox, 3, 1, 2, 1)

        self.seq1LedLbl = QLabel(self.groupBox_8)
        self.seq1LedLbl.setObjectName(u"seq1LedLbl")
        sizePolicy4.setHeightForWidth(self.seq1LedLbl.sizePolicy().hasHeightForWidth())
        self.seq1LedLbl.setSizePolicy(sizePolicy4)
        self.seq1LedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"	border: 3px solid black;\n"
"	background-color: #dd0000;\n"
"	color: black;\n"
"}")
        self.seq1LedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.seq1LedLbl, 3, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_8, 1, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 331, 21))
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
        self.menuFile.addAction(self.scoringLoadFromFileAction)
        self.menuSequence.addAction(self.seqLoadFromFileAction)
        self.menuHelp.addAction(self.helpAboutAction)
        self.menuResults.addAction(self.resultsLoadFromFileAction)
        self.menuResults.addAction(self.resultsShowAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.seqLoadFromFileAction.setText(QCoreApplication.translate("MainWindow", u"Load from file", None))
        self.helpAboutAction.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.scoringLoadFromFileAction.setText(QCoreApplication.translate("MainWindow", u"Load from file", None))
        self.resultsLoadFromFileAction.setText(QCoreApplication.translate("MainWindow", u"Load from file", None))
        self.resultsShowAction.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.selectSeqFirstBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sequence 1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sequence 2", None))
        self.selectSeqSecBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mismatch", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gap", None))
        self.fetchScoringBtn.setText(QCoreApplication.translate("MainWindow", u"Fetch scoring", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Active processes", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.seq2LedLbl.setText(QCoreApplication.translate("MainWindow", u"Seq2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.processBtn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.operationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.dotplotRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Dotplot", None))
        self.alignmentRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.seq1LedLbl.setText(QCoreApplication.translate("MainWindow", u"Seq1", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.menuSequence.setTitle(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuResults.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
    # retranslateUi

