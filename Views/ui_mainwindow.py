# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(520, 587)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: #333333;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(MainWindow)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(400, 400))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QWidget {\n"
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
"")
        self.createTaskTab = QWidget()
        self.createTaskTab.setObjectName(u"createTaskTab")
        sizePolicy.setHeightForWidth(self.createTaskTab.sizePolicy().hasHeightForWidth())
        self.createTaskTab.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.createTaskTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_4 = QGroupBox(self.createTaskTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)

        self.seq2ListWidget = QListWidget(self.groupBox_4)
        self.seq2ListWidget.setObjectName(u"seq2ListWidget")

        self.gridLayout_4.addWidget(self.seq2ListWidget, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.seq1ListWidget = QListWidget(self.groupBox_4)
        self.seq1ListWidget.setObjectName(u"seq1ListWidget")
        sizePolicy.setHeightForWidth(self.seq1ListWidget.sizePolicy().hasHeightForWidth())
        self.seq1ListWidget.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.seq1ListWidget, 1, 0, 1, 1)

        self.identifierLineEdit = QLineEdit(self.groupBox_4)
        self.identifierLineEdit.setObjectName(u"identifierLineEdit")
        self.identifierLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.identifierLineEdit, 2, 1, 1, 1)

        self.fetchSeqFromFileBtn = QPushButton(self.groupBox_4)
        self.fetchSeqFromFileBtn.setObjectName(u"fetchSeqFromFileBtn")

        self.gridLayout_4.addWidget(self.fetchSeqFromFileBtn, 4, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)

        self.fetchSeqFromInternetFile = QPushButton(self.groupBox_4)
        self.fetchSeqFromInternetFile.setObjectName(u"fetchSeqFromInternetFile")

        self.gridLayout_4.addWidget(self.fetchSeqFromInternetFile, 3, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.createTaskTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.fetchScoringBtn = QPushButton(self.groupBox_3)
        self.fetchScoringBtn.setObjectName(u"fetchScoringBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fetchScoringBtn.sizePolicy().hasHeightForWidth())
        self.fetchScoringBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.fetchScoringBtn, 4, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.matchLineEdit = QLineEdit(self.groupBox_3)
        self.matchLineEdit.setObjectName(u"matchLineEdit")
        self.matchLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.matchLineEdit, 0, 1, 1, 1)

        self.mismatchLineEdit = QLineEdit(self.groupBox_3)
        self.mismatchLineEdit.setObjectName(u"mismatchLineEdit")
        self.mismatchLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.mismatchLineEdit, 1, 1, 1, 1)

        self.gapLineEdit = QLineEdit(self.groupBox_3)
        self.gapLineEdit.setObjectName(u"gapLineEdit")
        self.gapLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.gapLineEdit, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.fetchScoringFromFileBtn = QPushButton(self.groupBox_3)
        self.fetchScoringFromFileBtn.setObjectName(u"fetchScoringFromFileBtn")
        sizePolicy2.setHeightForWidth(self.fetchScoringFromFileBtn.sizePolicy().hasHeightForWidth())
        self.fetchScoringFromFileBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.fetchScoringFromFileBtn, 5, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.createTaskTab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.activeProcListWidget = QListWidget(self.groupBox_6)
        self.activeProcListWidget.setObjectName(u"activeProcListWidget")

        self.gridLayout_2.addWidget(self.activeProcListWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.helpBtn = QPushButton(self.createTaskTab)
        self.helpBtn.setObjectName(u"helpBtn")

        self.gridLayout_5.addWidget(self.helpBtn, 2, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.createTaskTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.operationGroupBox = QGroupBox(self.groupBox_5)
        self.operationGroupBox.setObjectName(u"operationGroupBox")
        self.verticalLayout = QVBoxLayout(self.operationGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dotplotRadioBtn = QRadioButton(self.operationGroupBox)
        self.dotplotRadioBtn.setObjectName(u"dotplotRadioBtn")
        self.dotplotRadioBtn.setChecked(True)

        self.verticalLayout.addWidget(self.dotplotRadioBtn)

        self.alignmentRadioBtn = QRadioButton(self.operationGroupBox)
        self.alignmentRadioBtn.setObjectName(u"alignmentRadioBtn")

        self.verticalLayout.addWidget(self.alignmentRadioBtn)


        self.gridLayout.addWidget(self.operationGroupBox, 1, 0, 1, 2)

        self.seqsLedLbl = QLabel(self.groupBox_5)
        self.seqsLedLbl.setObjectName(u"seqsLedLbl")
        self.seqsLedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 20px;\n"
"	border: 3px solid black;\n"
"	background-color: #dd0000;\n"
"	color: black;\n"
"}")
        self.seqsLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.seqsLedLbl, 0, 0, 1, 1)

        self.processBtn = QPushButton(self.groupBox_5)
        self.processBtn.setObjectName(u"processBtn")

        self.gridLayout.addWidget(self.processBtn, 4, 0, 1, 2)

        self.scoringLedLbl = QLabel(self.groupBox_5)
        self.scoringLedLbl.setObjectName(u"scoringLedLbl")
        self.scoringLedLbl.setStyleSheet(u"QLabel {\n"
"	border-radius: 20px;\n"
"	border: 3px solid black;\n"
"	background-color: #dd0000;\n"
"	color: black;\n"
"}")
        self.scoringLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.scoringLedLbl, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 1, 1, 2, 1)

        self.tabWidget.addTab(self.createTaskTab, "")
        self.viewResultsTab = QWidget()
        self.viewResultsTab.setObjectName(u"viewResultsTab")
        sizePolicy.setHeightForWidth(self.viewResultsTab.sizePolicy().hasHeightForWidth())
        self.viewResultsTab.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.viewResultsTab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.showDotplotBtn = QPushButton(self.viewResultsTab)
        self.showDotplotBtn.setObjectName(u"showDotplotBtn")

        self.gridLayout_7.addWidget(self.showDotplotBtn, 2, 0, 1, 1)

        self.listWidget_4 = QListWidget(self.viewResultsTab)
        self.listWidget_4.setObjectName(u"listWidget_4")

        self.gridLayout_7.addWidget(self.listWidget_4, 1, 1, 1, 1)

        self.listWidget_5 = QListWidget(self.viewResultsTab)
        self.listWidget_5.setObjectName(u"listWidget_5")

        self.gridLayout_7.addWidget(self.listWidget_5, 1, 0, 1, 1)

        self.loadDotplotBtn = QPushButton(self.viewResultsTab)
        self.loadDotplotBtn.setObjectName(u"loadDotplotBtn")

        self.gridLayout_7.addWidget(self.loadDotplotBtn, 0, 0, 1, 1)

        self.loadAlignmentBtn = QPushButton(self.viewResultsTab)
        self.loadAlignmentBtn.setObjectName(u"loadAlignmentBtn")

        self.gridLayout_7.addWidget(self.loadAlignmentBtn, 0, 1, 1, 1)

        self.showAlignmentBtn = QPushButton(self.viewResultsTab)
        self.showAlignmentBtn.setObjectName(u"showAlignmentBtn")

        self.gridLayout_7.addWidget(self.showAlignmentBtn, 2, 1, 1, 1)

        self.tabWidget.addTab(self.viewResultsTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter identifier", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sequence 1", None))
        self.fetchSeqFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Fetch sequence from file", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sequence 2", None))
        self.fetchSeqFromInternetFile.setText(QCoreApplication.translate("MainWindow", u"Fetch sequence from the Internet", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.fetchScoringBtn.setText(QCoreApplication.translate("MainWindow", u"Fetch scoring", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mismatch", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gap", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.fetchScoringFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Fetch scoring from file", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Active processes", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.operationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.dotplotRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Dotplot", None))
        self.alignmentRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.seqsLedLbl.setText(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.processBtn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.scoringLedLbl.setText(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createTaskTab), QCoreApplication.translate("MainWindow", u"Create task", None))
        self.showDotplotBtn.setText(QCoreApplication.translate("MainWindow", u"Show selected", None))
        self.loadDotplotBtn.setText(QCoreApplication.translate("MainWindow", u"Load dotplot", None))
        self.loadAlignmentBtn.setText(QCoreApplication.translate("MainWindow", u"Load alignment", None))
        self.showAlignmentBtn.setText(QCoreApplication.translate("MainWindow", u"Show selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewResultsTab), QCoreApplication.translate("MainWindow", u"View results", None))
    # retranslateUi

