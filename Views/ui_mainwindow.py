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

from Views.dndListWidget import DndListWidget
from Views.activeProcTableWidget import ActiveProcTableWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 472)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.helpAboutAction = QAction(MainWindow)
        self.helpAboutAction.setObjectName(u"helpAboutAction")
        self.viewOperationAction = QAction(MainWindow)
        self.viewOperationAction.setObjectName(u"viewOperationAction")
        self.seqFromNetAction = QAction(MainWindow)
        self.seqFromNetAction.setObjectName(u"seqFromNetAction")
        self.viewResultsAction = QAction(MainWindow)
        self.viewResultsAction.setObjectName(u"viewResultsAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	font: \"Times New Roman\";\n"
"    font-size: 14px;\n"
"	color: white;\n"
"}\n"
"QLabel {\n"
"	color: white;\n"
"	font: italic \"Times New Roman\";\n"
"}\n"
"QLineEdit {\n"
"	border-radius: 8px;\n"
"	border: 1px solid white;\n"
"	background-color: #999999;\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border-radius: 8px;\n"
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
"    stop: 0.3 darkgray,\n"
"    stop: 0.6 gray,\n"
"    stop: 0.8 gray,\n"
"    stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 4px solid green;\n"
"}\n"
"\n"
"QListView {\n"
"	backgro"
                        "und: transparent;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QTabWidget {\n"
"	background: transparent;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background-color: #333333;\n"
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
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.operationGroupBox = QGroupBox(self.centralwidget)
        self.operationGroupBox.setObjectName(u"operationGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operationGroupBox.sizePolicy().hasHeightForWidth())
        self.operationGroupBox.setSizePolicy(sizePolicy)
        self.operationGroupBox.setMinimumSize(QSize(0, 10))
        self.operationGroupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.operationGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 9, 2, 9)
        self.processBtn = QPushButton(self.operationGroupBox)
        self.processBtn.setObjectName(u"processBtn")
        sizePolicy.setHeightForWidth(self.processBtn.sizePolicy().hasHeightForWidth())
        self.processBtn.setSizePolicy(sizePolicy)
        self.processBtn.setMinimumSize(QSize(0, 10))

        self.gridLayout_2.addWidget(self.processBtn, 3, 0, 1, 1)

        self.dotplotRadioBtn = QRadioButton(self.operationGroupBox)
        self.dotplotRadioBtn.setObjectName(u"dotplotRadioBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dotplotRadioBtn.sizePolicy().hasHeightForWidth())
        self.dotplotRadioBtn.setSizePolicy(sizePolicy1)
        self.dotplotRadioBtn.setMinimumSize(QSize(0, 10))
        self.dotplotRadioBtn.setLayoutDirection(Qt.LeftToRight)
        self.dotplotRadioBtn.setStyleSheet(u"")
        self.dotplotRadioBtn.setChecked(True)
        self.dotplotRadioBtn.setAutoRepeatInterval(5)

        self.gridLayout_2.addWidget(self.dotplotRadioBtn, 0, 0, 1, 1)

        self.alignmentRadioBtn = QRadioButton(self.operationGroupBox)
        self.alignmentRadioBtn.setObjectName(u"alignmentRadioBtn")
        sizePolicy1.setHeightForWidth(self.alignmentRadioBtn.sizePolicy().hasHeightForWidth())
        self.alignmentRadioBtn.setSizePolicy(sizePolicy1)
        self.alignmentRadioBtn.setMinimumSize(QSize(0, 10))

        self.gridLayout_2.addWidget(self.alignmentRadioBtn, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.operationGroupBox, 2, 6, 3, 1)

        self.processesGroupBox = QGroupBox(self.centralwidget)
        self.processesGroupBox.setObjectName(u"processesGroupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.processesGroupBox.sizePolicy().hasHeightForWidth())
        self.processesGroupBox.setSizePolicy(sizePolicy2)
        self.processesGroupBox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.gridLayout_11 = QGridLayout(self.processesGroupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 9, -1, -1)
        self.activeProcTableWidget = ActiveProcTableWidget(self.processesGroupBox)
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
        self.activeProcTableWidget.setFocusPolicy(Qt.NoFocus)
        self.activeProcTableWidget.setStyleSheet(u"QTableWidget {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	color: white;\n"
"	background-color: rgba(179, 179, 179, 102);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	color: white;\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}")
        self.activeProcTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.activeProcTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.activeProcTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.activeProcTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.activeProcTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.activeProcTableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.activeProcTableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.activeProcTableWidget.horizontalHeader().setHighlightSections(False)
        self.activeProcTableWidget.verticalHeader().setVisible(False)
        self.activeProcTableWidget.verticalHeader().setHighlightSections(False)

        self.gridLayout_11.addWidget(self.activeProcTableWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.processesGroupBox, 5, 2, 5, 5)

        self.seqGroupBox = QGroupBox(self.centralwidget)
        self.seqGroupBox.setObjectName(u"seqGroupBox")
        sizePolicy2.setHeightForWidth(self.seqGroupBox.sizePolicy().hasHeightForWidth())
        self.seqGroupBox.setSizePolicy(sizePolicy2)
        self.seqGroupBox.setMinimumSize(QSize(50, 0))
        self.seqGroupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.seqGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.selectSeqSecBtn = QPushButton(self.seqGroupBox)
        self.selectSeqSecBtn.setObjectName(u"selectSeqSecBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.selectSeqSecBtn.sizePolicy().hasHeightForWidth())
        self.selectSeqSecBtn.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.selectSeqSecBtn, 9, 1, 1, 1)

        self.seq1ListWidget = DndListWidget(self.seqGroupBox)
        self.seq1ListWidget.setObjectName(u"seq1ListWidget")
        sizePolicy2.setHeightForWidth(self.seq1ListWidget.sizePolicy().hasHeightForWidth())
        self.seq1ListWidget.setSizePolicy(sizePolicy2)
        self.seq1ListWidget.setFocusPolicy(Qt.NoFocus)
        self.seq1ListWidget.setStyleSheet(u"QListView::item {\n"
"	color: white;\n"
"	background-color: rgba(179, 179, 179, 102);\n"
"	border-bottom: 2px solid black;\n"
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

        self.gridLayout.addWidget(self.seq1ListWidget, 0, 0, 9, 2)

        self.selectSeqFirstBtn = QPushButton(self.seqGroupBox)
        self.selectSeqFirstBtn.setObjectName(u"selectSeqFirstBtn")
        sizePolicy3.setHeightForWidth(self.selectSeqFirstBtn.sizePolicy().hasHeightForWidth())
        self.selectSeqFirstBtn.setSizePolicy(sizePolicy3)
        self.selectSeqFirstBtn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.selectSeqFirstBtn, 9, 0, 1, 1)


        self.gridLayout_6.addWidget(self.seqGroupBox, 0, 0, 10, 2)

        self.indicatorsGroupBox = QGroupBox(self.centralwidget)
        self.indicatorsGroupBox.setObjectName(u"indicatorsGroupBox")
        sizePolicy.setHeightForWidth(self.indicatorsGroupBox.sizePolicy().hasHeightForWidth())
        self.indicatorsGroupBox.setSizePolicy(sizePolicy)
        self.indicatorsGroupBox.setMinimumSize(QSize(0, 100))
        self.indicatorsGroupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.indicatorsGroupBox)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 2)
        self.internetConnLbl = QLabel(self.indicatorsGroupBox)
        self.internetConnLbl.setObjectName(u"internetConnLbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.internetConnLbl.sizePolicy().hasHeightForWidth())
        self.internetConnLbl.setSizePolicy(sizePolicy4)
        self.internetConnLbl.setMinimumSize(QSize(60, 60))
        self.internetConnLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.internetConnLbl, 1, 3, 2, 1)

        self.secSeqLbl = QLabel(self.indicatorsGroupBox)
        self.secSeqLbl.setObjectName(u"secSeqLbl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.secSeqLbl.sizePolicy().hasHeightForWidth())
        self.secSeqLbl.setSizePolicy(sizePolicy5)
        self.secSeqLbl.setMinimumSize(QSize(50, 20))
        self.secSeqLbl.setAlignment(Qt.AlignCenter)
        self.secSeqLbl.setWordWrap(True)

        self.gridLayout_3.addWidget(self.secSeqLbl, 0, 1, 1, 1)

        self.scoringLedLbl = QLabel(self.indicatorsGroupBox)
        self.scoringLedLbl.setObjectName(u"scoringLedLbl")
        sizePolicy4.setHeightForWidth(self.scoringLedLbl.sizePolicy().hasHeightForWidth())
        self.scoringLedLbl.setSizePolicy(sizePolicy4)
        self.scoringLedLbl.setMinimumSize(QSize(60, 60))
        self.scoringLedLbl.setStyleSheet(u"")
        self.scoringLedLbl.setScaledContents(False)
        self.scoringLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.scoringLedLbl, 1, 2, 2, 1)

        self.seqFirstLedLbl = QLabel(self.indicatorsGroupBox)
        self.seqFirstLedLbl.setObjectName(u"seqFirstLedLbl")
        sizePolicy.setHeightForWidth(self.seqFirstLedLbl.sizePolicy().hasHeightForWidth())
        self.seqFirstLedLbl.setSizePolicy(sizePolicy)
        self.seqFirstLedLbl.setMinimumSize(QSize(60, 60))
        self.seqFirstLedLbl.setStyleSheet(u"")
        self.seqFirstLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.seqFirstLedLbl, 1, 0, 2, 1)

        self.firstSeqLbl = QLabel(self.indicatorsGroupBox)
        self.firstSeqLbl.setObjectName(u"firstSeqLbl")
        sizePolicy4.setHeightForWidth(self.firstSeqLbl.sizePolicy().hasHeightForWidth())
        self.firstSeqLbl.setSizePolicy(sizePolicy4)
        self.firstSeqLbl.setMinimumSize(QSize(50, 20))
        self.firstSeqLbl.setAlignment(Qt.AlignCenter)
        self.firstSeqLbl.setWordWrap(True)

        self.gridLayout_3.addWidget(self.firstSeqLbl, 0, 0, 1, 1)

        self.seqSecLedLbl = QLabel(self.indicatorsGroupBox)
        self.seqSecLedLbl.setObjectName(u"seqSecLedLbl")
        sizePolicy.setHeightForWidth(self.seqSecLedLbl.sizePolicy().hasHeightForWidth())
        self.seqSecLedLbl.setSizePolicy(sizePolicy)
        self.seqSecLedLbl.setMinimumSize(QSize(60, 60))
        self.seqSecLedLbl.setStyleSheet(u"")
        self.seqSecLedLbl.setScaledContents(False)
        self.seqSecLedLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.seqSecLedLbl, 1, 1, 2, 1)

        self.internetLbl = QLabel(self.indicatorsGroupBox)
        self.internetLbl.setObjectName(u"internetLbl")
        sizePolicy5.setHeightForWidth(self.internetLbl.sizePolicy().hasHeightForWidth())
        self.internetLbl.setSizePolicy(sizePolicy5)
        self.internetLbl.setMinimumSize(QSize(50, 20))
        self.internetLbl.setAlignment(Qt.AlignCenter)
        self.internetLbl.setWordWrap(True)

        self.gridLayout_3.addWidget(self.internetLbl, 0, 3, 1, 1)

        self.scoringLbl = QLabel(self.indicatorsGroupBox)
        self.scoringLbl.setObjectName(u"scoringLbl")
        sizePolicy5.setHeightForWidth(self.scoringLbl.sizePolicy().hasHeightForWidth())
        self.scoringLbl.setSizePolicy(sizePolicy5)
        self.scoringLbl.setMinimumSize(QSize(50, 20))
        self.scoringLbl.setAlignment(Qt.AlignCenter)
        self.scoringLbl.setWordWrap(True)

        self.gridLayout_3.addWidget(self.scoringLbl, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.indicatorsGroupBox, 2, 2, 3, 4)

        self.scoringGroupBox = QGroupBox(self.centralwidget)
        self.scoringGroupBox.setObjectName(u"scoringGroupBox")
        sizePolicy.setHeightForWidth(self.scoringGroupBox.sizePolicy().hasHeightForWidth())
        self.scoringGroupBox.setSizePolicy(sizePolicy)
        self.scoringGroupBox.setMinimumSize(QSize(0, 0))
        self.scoringGroupBox.setSizeIncrement(QSize(1, 0))
        self.scoringGroupBox.setBaseSize(QSize(0, 0))
        self.scoringGroupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.scoringGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(5, 9, 5, 9)
        self.fetchScoringBtn = QPushButton(self.scoringGroupBox)
        self.fetchScoringBtn.setObjectName(u"fetchScoringBtn")
        sizePolicy.setHeightForWidth(self.fetchScoringBtn.sizePolicy().hasHeightForWidth())
        self.fetchScoringBtn.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.fetchScoringBtn, 1, 3, 1, 1)

        self.matchLineEdit = QLineEdit(self.scoringGroupBox)
        self.matchLineEdit.setObjectName(u"matchLineEdit")
        sizePolicy.setHeightForWidth(self.matchLineEdit.sizePolicy().hasHeightForWidth())
        self.matchLineEdit.setSizePolicy(sizePolicy)
        self.matchLineEdit.setMinimumSize(QSize(0, 0))
        self.matchLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.matchLineEdit.setAlignment(Qt.AlignCenter)
        self.matchLineEdit.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.matchLineEdit, 1, 0, 1, 1)

        self.gapLineEdit = QLineEdit(self.scoringGroupBox)
        self.gapLineEdit.setObjectName(u"gapLineEdit")
        sizePolicy.setHeightForWidth(self.gapLineEdit.sizePolicy().hasHeightForWidth())
        self.gapLineEdit.setSizePolicy(sizePolicy)
        self.gapLineEdit.setMinimumSize(QSize(0, 0))
        self.gapLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.gapLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.gapLineEdit, 1, 2, 1, 1)

        self.mismatchLineEdit = QLineEdit(self.scoringGroupBox)
        self.mismatchLineEdit.setObjectName(u"mismatchLineEdit")
        sizePolicy.setHeightForWidth(self.mismatchLineEdit.sizePolicy().hasHeightForWidth())
        self.mismatchLineEdit.setSizePolicy(sizePolicy)
        self.mismatchLineEdit.setMinimumSize(QSize(0, 0))
        self.mismatchLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.mismatchLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mismatchLineEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(self.scoringGroupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_10 = QLabel(self.scoringGroupBox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_9 = QLabel(self.scoringGroupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.scoringGroupBox, 0, 2, 2, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1060, 23))
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy7)
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"	border: 1px solid white;\n"
"	background: transparent;\n"
"	color: white;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"	color: white;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"	border: 1px solid white;\n"
"	color: white;\n"
"}")
        self.menuSequence = QMenu(self.menubar)
        self.menuSequence.setObjectName(u"menuSequence")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuResults = QMenu(self.menubar)
        self.menuResults.setObjectName(u"menuResults")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSequence.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSequence.addAction(self.seqFromNetAction)
        self.menuHelp.addAction(self.helpAboutAction)
        self.menuResults.addAction(self.viewOperationAction)
        self.menuResults.addAction(self.viewResultsAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.helpAboutAction.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.viewOperationAction.setText(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.seqFromNetAction.setText(QCoreApplication.translate("MainWindow", u"Get from the Internet", None))
        self.viewResultsAction.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.operationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.processBtn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.dotplotRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Dotplot", None))
        self.alignmentRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.processesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Active processes", None))
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
        self.seqGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.selectSeqSecBtn.setText(QCoreApplication.translate("MainWindow", u"Select Second", None))
        self.selectSeqFirstBtn.setText(QCoreApplication.translate("MainWindow", u"Select First", None))
        self.indicatorsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Indicators", None))
        self.internetConnLbl.setText("")
        self.secSeqLbl.setText(QCoreApplication.translate("MainWindow", u"Second Sequence", None))
        self.scoringLedLbl.setText("")
        self.seqFirstLedLbl.setText("")
        self.firstSeqLbl.setText(QCoreApplication.translate("MainWindow", u"First Sequence", None))
        self.seqSecLedLbl.setText("")
        self.internetLbl.setText(QCoreApplication.translate("MainWindow", u"Internet", None))
        self.scoringLbl.setText(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.scoringGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Scoring", None))
        self.fetchScoringBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.matchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type in...", None))
        self.gapLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type in...", None))
        self.mismatchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type in...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mismatch", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gap", None))
        self.menuSequence.setTitle(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuResults.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

