# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(208, 118)
        Dialog.setStyleSheet(u"QDialog {\n"
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
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.textEdit = QPlainTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setFocusPolicy(Qt.ClickFocus)
        self.textEdit.setStyleSheet(u"")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Info", None))
    # retranslateUi

