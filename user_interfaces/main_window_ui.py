# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 550)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"MainWindow {\n"
"background-color: black; \n"
"background-image:url(./images/background_image.png); \n"
"background-repeat: no-repeat;\n"
"}")
        self.credits_action_button = QAction(MainWindow)
        self.credits_action_button.setObjectName(u"credits_action_button")
        self.help_page_action_button = QAction(MainWindow)
        self.help_page_action_button.setObjectName(u"help_page_action_button")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setAutoFillBackground(False)
        self.central_widget.setStyleSheet(u"#central_widget {\n"
"	opacity: 0;\n"
"}")
        self.skull_downloader_logo_label = QLabel(self.central_widget)
        self.skull_downloader_logo_label.setObjectName(u"skull_downloader_logo_label")
        self.skull_downloader_logo_label.setGeometry(QRect(150, 50, 200, 200))
        self.skull_downloader_logo_label.setPixmap(QPixmap(u":/logos/skull_logo.png"))
        self.skull_downloader_logo_label.setScaledContents(True)
        self.media_format_label = QLabel(self.central_widget)
        self.media_format_label.setObjectName(u"media_format_label")
        self.media_format_label.setGeometry(QRect(70, 340, 150, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.media_format_label.setFont(font)
        self.media_format_label.setStyleSheet(u"#media_format_label {\n"
"	color: white;\n"
"}")
        self.url_label = QLabel(self.central_widget)
        self.url_label.setObjectName(u"url_label")
        self.url_label.setGeometry(QRect(70, 280, 150, 30))
        self.url_label.setFont(font)
        self.url_label.setStyleSheet(u"#url_label {\n"
"	color: white;\n"
"}")
        self.media_format_choice_combo_box = QComboBox(self.central_widget)
        self.media_format_choice_combo_box.addItem("")
        self.media_format_choice_combo_box.addItem("")
        self.media_format_choice_combo_box.setObjectName(u"media_format_choice_combo_box")
        self.media_format_choice_combo_box.setGeometry(QRect(230, 340, 100, 30))
        self.url_line_edit = QLineEdit(self.central_widget)
        self.url_line_edit.setObjectName(u"url_line_edit")
        self.url_line_edit.setGeometry(QRect(230, 280, 200, 30))
        self.download_button = QPushButton(self.central_widget)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(340, 340, 91, 30))
        self.info_label = QLabel(self.central_widget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(50, 450, 400, 70))
        self.info_label.setStyleSheet(u"#info_label {\n"
"	color: white;\n"
"}")
        self.info_label.setWordWrap(True)
        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 500, 22))
        self.help_menu = QMenu(self.menu_bar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.menu_bar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menu_bar.addAction(self.help_menu.menuAction())
        self.help_menu.addAction(self.credits_action_button)
        self.help_menu.addAction(self.help_page_action_button)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Skull Downloader", None))
        self.credits_action_button.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.help_page_action_button.setText(QCoreApplication.translate("MainWindow", u"Help Page", None))
        self.skull_downloader_logo_label.setText("")
        self.media_format_label.setText(QCoreApplication.translate("MainWindow", u"Out put format", None))
        self.url_label.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.media_format_choice_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Audio", None))
        self.media_format_choice_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Video", None))

        self.url_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the url here...", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.info_label.setText("")
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

