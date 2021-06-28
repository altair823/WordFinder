# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finder_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WordFinderGUI(object):
    def setupUi(self, WordFinderGUI):
        WordFinderGUI.setObjectName("WordFinderGUI")
        WordFinderGUI.resize(896, 625)
        WordFinderGUI.setStyleSheet("background-color: rgb(100, 98, 100);")
        self.verticalLayoutWidget = QtWidgets.QWidget(WordFinderGUI)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 171, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_bar = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_bar.setStyleSheet("color: rgb(255, 255, 255);")
        self.search_bar.setDragEnabled(True)
        self.search_bar.setObjectName("search_bar")
        self.verticalLayout.addWidget(self.search_bar)
        self.search = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search.setStyleSheet("background-color: rgb(132, 142, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.search.setObjectName("search")
        self.verticalLayout.addWidget(self.search)
        self.gridLayoutWidget = QtWidgets.QWidget(WordFinderGUI)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 10, 681, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 664, 252))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.naver_search_result = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.naver_search_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.naver_search_result.setText("")
        self.naver_search_result.setWordWrap(True)
        self.naver_search_result.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.naver_search_result.setObjectName("naver_search_result")
        self.verticalLayout_2.addWidget(self.naver_search_result)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.naver_page = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.naver_page.setMaximumSize(QtCore.QSize(100, 16777215))
        self.naver_page.setStyleSheet("background-color: rgb(147, 202, 255);")
        self.naver_page.setObjectName("naver_page")
        self.gridLayout.addWidget(self.naver_page, 0, 1, 1, 1)
        self.naver_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.naver_label.setEnabled(True)
        self.naver_label.setMinimumSize(QtCore.QSize(0, 0))
        self.naver_label.setMaximumSize(QtCore.QSize(561, 50))
        self.naver_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.naver_label.setAlignment(QtCore.Qt.AlignCenter)
        self.naver_label.setObjectName("naver_label")
        self.gridLayout.addWidget(self.naver_label, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(WordFinderGUI)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(190, 310, 681, 311))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 664, 272))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wiki_search_result = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.wiki_search_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wiki_search_result.setText("")
        self.wiki_search_result.setWordWrap(True)
        self.wiki_search_result.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.wiki_search_result.setObjectName("wiki_search_result")
        self.verticalLayout_3.addWidget(self.wiki_search_result)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_2.addWidget(self.scrollArea_2, 1, 0, 1, 2)
        self.wiki_page = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.wiki_page.setMaximumSize(QtCore.QSize(100, 16777215))
        self.wiki_page.setStyleSheet("background-color: rgb(147, 202, 255);")
        self.wiki_page.setObjectName("wiki_page")
        self.gridLayout_2.addWidget(self.wiki_page, 0, 1, 1, 1)
        self.wiki_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.wiki_label.setEnabled(True)
        self.wiki_label.setMinimumSize(QtCore.QSize(0, 0))
        self.wiki_label.setMaximumSize(QtCore.QSize(561, 50))
        self.wiki_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.wiki_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wiki_label.setObjectName("wiki_label")
        self.gridLayout_2.addWidget(self.wiki_label, 0, 0, 1, 1)
        self.update_btn = QtWidgets.QPushButton(WordFinderGUI)
        self.update_btn.setGeometry(QtCore.QRect(40, 440, 113, 32))
        self.update_btn.setStyleSheet("background-color: rgb(235, 232, 237);")
        self.update_btn.setObjectName("update_btn")

        self.retranslateUi(WordFinderGUI)
        QtCore.QMetaObject.connectSlotsByName(WordFinderGUI)

    def retranslateUi(self, WordFinderGUI):
        _translate = QtCore.QCoreApplication.translate
        WordFinderGUI.setWindowTitle(_translate("WordFinderGUI", "Dialog"))
        self.search.setText(_translate("WordFinderGUI", "검색"))
        self.naver_page.setText(_translate("WordFinderGUI", "페이지 방문"))
        self.naver_label.setText(_translate("WordFinderGUI", "네이버 사전"))
        self.wiki_page.setText(_translate("WordFinderGUI", "페이지 방문"))
        self.wiki_label.setText(_translate("WordFinderGUI", "위키백과"))
        self.update_btn.setText(_translate("WordFinderGUI", "업데이트"))

