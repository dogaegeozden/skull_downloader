# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credits_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreditsDialog(object):
    def setupUi(self, CreditsDialog):
        if not CreditsDialog.objectName():
            CreditsDialog.setObjectName(u"CreditsDialog")
        CreditsDialog.resize(400, 200)
        self.label = QLabel(CreditsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 85, 200, 30))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.retranslateUi(CreditsDialog)

        QMetaObject.connectSlotsByName(CreditsDialog)
    # setupUi

    def retranslateUi(self, CreditsDialog):
        CreditsDialog.setWindowTitle(QCoreApplication.translate("CreditsDialog", u"Credits", None))
        self.label.setText(QCoreApplication.translate("CreditsDialog", u"Made by Doga Ege Ozden", None))
    # retranslateUi

