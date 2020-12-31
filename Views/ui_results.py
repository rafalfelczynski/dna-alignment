# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Views.dotplotsTableWidget import DotplotsTableWidget
from Views.alignmentsTableWidget import AlignmentsTableWidget


class Ui_ResultsWidget(object):
    def setupUi(self, ResultsWidget):
        if not ResultsWidget.objectName():
            ResultsWidget.setObjectName(u"ResultsWidget")
        ResultsWidget.resize(642, 561)
        ResultsWidget.setStyleSheet(u"QWidget {\n"
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
"	backgr"
                        "ound: transparent;\n"
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
"QTabWidget::pane {\n"
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
        self.verticalLayout_2 = QVBoxLayout(ResultsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dotpGroupBox = QGroupBox(ResultsWidget)
        self.dotpGroupBox.setObjectName(u"dotpGroupBox")
        self.dotpGroupBox.setStyleSheet(u"QGroupBox {\n"
"	background: transparent;\n"
"}")
        self.dotpGroupBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.dotpGroupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.dotpGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dotpTableWidget = DotplotsTableWidget(self.dotpGroupBox)
        if (self.dotpTableWidget.columnCount() < 2):
            self.dotpTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.dotpTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dotpTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.dotpTableWidget.setObjectName(u"dotpTableWidget")
        self.dotpTableWidget.setFocusPolicy(Qt.NoFocus)
        self.dotpTableWidget.setStyleSheet(u"QTableWidget {\n"
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
        self.dotpTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dotpTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dotpTableWidget.setColumnCount(2)
        self.dotpTableWidget.horizontalHeader().setHighlightSections(False)
        self.dotpTableWidget.verticalHeader().setVisible(False)
        self.dotpTableWidget.verticalHeader().setHighlightSections(False)

        self.gridLayout.addWidget(self.dotpTableWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.dotpGroupBox)

        self.alignGroupBox = QGroupBox(ResultsWidget)
        self.alignGroupBox.setObjectName(u"alignGroupBox")
        self.alignGroupBox.setStyleSheet(u"QGroupBox {\n"
"	background: transparent;\n"
"}")
        self.alignGroupBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.alignGroupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.alignGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.alignTableWidget = AlignmentsTableWidget(self.alignGroupBox)
        if (self.alignTableWidget.columnCount() < 5):
            self.alignTableWidget.setColumnCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.alignTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.alignTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.alignTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.alignTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.alignTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        self.alignTableWidget.setObjectName(u"alignTableWidget")
        self.alignTableWidget.setFocusPolicy(Qt.NoFocus)
        self.alignTableWidget.setStyleSheet(u"QTableWidget {\n"
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
        self.alignTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.alignTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.alignTableWidget.horizontalHeader().setHighlightSections(False)
        self.alignTableWidget.verticalHeader().setVisible(False)
        self.alignTableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.alignTableWidget)


        self.verticalLayout_2.addWidget(self.alignGroupBox)


        self.retranslateUi(ResultsWidget)

        QMetaObject.connectSlotsByName(ResultsWidget)
    # setupUi

    def retranslateUi(self, ResultsWidget):
        ResultsWidget.setWindowTitle(QCoreApplication.translate("ResultsWidget", u"Results", None))
        self.dotpGroupBox.setTitle(QCoreApplication.translate("ResultsWidget", u"Dotplots", None))
        ___qtablewidgetitem = self.dotpTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ResultsWidget", u"Sequence 1", None));
        ___qtablewidgetitem1 = self.dotpTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ResultsWidget", u"Sequence 2", None));
        self.alignGroupBox.setTitle(QCoreApplication.translate("ResultsWidget", u"Alignments", None))
        ___qtablewidgetitem2 = self.alignTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ResultsWidget", u"Sequence 1", None));
        ___qtablewidgetitem3 = self.alignTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ResultsWidget", u"Sequence 2", None));
        ___qtablewidgetitem4 = self.alignTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ResultsWidget", u"Match", None));
        ___qtablewidgetitem5 = self.alignTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ResultsWidget", u"Mismatch", None));
        ___qtablewidgetitem6 = self.alignTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ResultsWidget", u"Gap", None));
    # retranslateUi

