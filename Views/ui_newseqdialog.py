# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_seq_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewSequence(object):
    def setupUi(self, NewSequence):
        if not NewSequence.objectName():
            NewSequence.setObjectName(u"NewSequence")
        NewSequence.resize(174, 110)
        NewSequence.setStyleSheet(u"QDialog {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: #333333;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    border: 2px solid white;\n"
"	background-color: #333333;\n"
"    font-size: 14px;\n"
"	width: 50px;\n"
"}")
        NewSequence.setSizeGripEnabled(False)
        NewSequence.setModal(False)
        self.gridLayout_2 = QGridLayout(NewSequence)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(NewSequence)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.identifierLineEdit = QLineEdit(self.widget)
        self.identifierLineEdit.setObjectName(u"identifierLineEdit")
        self.identifierLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.identifierLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.identifierLineEdit, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(NewSequence)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(NewSequence)
        self.buttonBox.accepted.connect(NewSequence.accept)
        self.buttonBox.rejected.connect(NewSequence.reject)

        QMetaObject.connectSlotsByName(NewSequence)
    # setupUi

    def retranslateUi(self, NewSequence):
        NewSequence.setWindowTitle(QCoreApplication.translate("NewSequence", u"New Sequence", None))
        self.label.setText(QCoreApplication.translate("NewSequence", u"Insert identifier", None))
    # retranslateUi

