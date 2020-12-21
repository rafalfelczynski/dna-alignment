# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_dialog.ui'
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
        Dialog.resize(203, 144)
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
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)

        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Are you sure?", None))
    # retranslateUi

