# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.wiki_gopage = QtWidgets.QPushButton(self.centralwidget)
        self.wiki_gopage.setMaximumSize(QtCore.QSize(150, 50))
        self.wiki_gopage.setObjectName("wiki_gopage")
        self.gridLayout_4.addWidget(self.wiki_gopage, 1, 1, 1, 1)
        self.wiki_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.wiki_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.wiki_scroll.setWidgetResizable(True)
        self.wiki_scroll.setObjectName("wiki_scroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 360, 592))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.wiki_result = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.wiki_result.setText("")
        self.wiki_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.wiki_result.setWordWrap(True)
        self.wiki_result.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.wiki_result.setObjectName("wiki_result")
        self.gridLayout_5.addWidget(self.wiki_result, 0, 0, 1, 1)
        self.wiki_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.wiki_scroll, 2, 0, 1, 2)
        self.wiki_label = QtWidgets.QLabel(self.centralwidget)
        self.wiki_label.setStyleSheet("border-color: rgb(129, 127, 130);")
        self.wiki_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wiki_label.setObjectName("wiki_label")
        self.gridLayout_4.addWidget(self.wiki_label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bar.setObjectName("search_bar")
        self.verticalLayout.addWidget(self.search_bar)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.search_button.setObjectName("search_button")
        self.verticalLayout.addWidget(self.search_button)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.naver_label = QtWidgets.QLabel(self.centralwidget)
        self.naver_label.setAlignment(QtCore.Qt.AlignCenter)
        self.naver_label.setObjectName("naver_label")
        self.gridLayout.addWidget(self.naver_label, 0, 0, 1, 1)
        self.naver_gopage = QtWidgets.QPushButton(self.centralwidget)
        self.naver_gopage.setMaximumSize(QtCore.QSize(150, 50))
        self.naver_gopage.setObjectName("naver_gopage")
        self.gridLayout.addWidget(self.naver_gopage, 0, 1, 1, 1)
        self.naver_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.naver_scroll.setWidgetResizable(True)
        self.naver_scroll.setObjectName("naver_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 592))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.naver_result = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.naver_result.setText("")
        self.naver_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.naver_result.setWordWrap(True)
        self.naver_result.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.naver_result.setObjectName("naver_result")
        self.gridLayout_3.addWidget(self.naver_result, 0, 0, 1, 1)
        self.naver_scroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.naver_scroll, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 24))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_info = QtWidgets.QMenu(self.menubar)
        self.menu_info.setObjectName("menu_info")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_file_save = QtWidgets.QAction(MainWindow)
        self.menu_file_save.setObjectName("menu_file_save")
        self.menu_file_open = QtWidgets.QAction(MainWindow)
        self.menu_file_open.setObjectName("menu_file_open")
        self.menu_info_help = QtWidgets.QAction(MainWindow)
        self.menu_info_help.setObjectName("menu_info_help")
        self.menu_info_update = QtWidgets.QAction(MainWindow)
        self.menu_info_update.setObjectName("menu_info_update")
        self.menu_info_program_ver = QtWidgets.QAction(MainWindow)
        self.menu_info_program_ver.setObjectName("menu_info_program_ver")
        self.menu_file.addAction(self.menu_file_save)
        self.menu_file.addAction(self.menu_file_open)
        self.menu_info.addAction(self.menu_info_help)
        self.menu_info.addAction(self.menu_info_update)
        self.menu_info.addAction(self.menu_info_program_ver)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_info.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wiki_gopage.setText(_translate("MainWindow", "웹 페이지로 가기"))
        self.wiki_label.setText(_translate("MainWindow", "위키백과"))
        self.search_button.setText(_translate("MainWindow", "검색"))
        self.naver_label.setText(_translate("MainWindow", "네이버"))
        self.naver_gopage.setText(_translate("MainWindow", "웹 페이지로 가기"))
        self.menu_file.setTitle(_translate("MainWindow", "파일"))
        self.menu_info.setTitle(_translate("MainWindow", "정보"))
        self.menu_file_save.setText(_translate("MainWindow", "저장"))
        self.menu_file_open.setText(_translate("MainWindow", "불러오기"))
        self.menu_info_help.setText(_translate("MainWindow", "도움말"))
        self.menu_info_update.setText(_translate("MainWindow", "업데이트"))
        self.menu_info_program_ver.setText(_translate("MainWindow", "프로그램 정보"))
