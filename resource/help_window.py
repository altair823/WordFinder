# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help_window(object):
    def setupUi(self, help_window):
        help_window.setObjectName("help_window")
        help_window.resize(421, 721)
        self.gridLayout = QtWidgets.QGridLayout(help_window)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(help_window)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 395, 660))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.help_text_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(15)
        self.help_text_label.setFont(font)
        self.help_text_label.setText("")
        self.help_text_label.setWordWrap(True)
        self.help_text_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.help_text_label.setObjectName("help_text_label")
        self.gridLayout_2.addWidget(self.help_text_label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(help_window)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

    def retranslateUi(self, help_window):
        _translate = QtCore.QCoreApplication.translate
        help_window.setWindowTitle(_translate("help_window", "Dialog"))
        self.label.setText(_translate("help_window", "도움말"))

