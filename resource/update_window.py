# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_dialog(object):
    def setupUi(self, update_dialog):
        update_dialog.setObjectName("update_dialog")
        update_dialog.resize(396, 115)
        update_dialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(update_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.update_label = QtWidgets.QLabel(update_dialog)
        self.update_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.update_label.setFont(font)
        self.update_label.setStyleSheet("")
        self.update_label.setAlignment(QtCore.Qt.AlignCenter)
        self.update_label.setObjectName("update_label")
        self.verticalLayout.addWidget(self.update_label)
        self.progress_bar = QtWidgets.QProgressBar(update_dialog)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(update_dialog)
        QtCore.QMetaObject.connectSlotsByName(update_dialog)

    def retranslateUi(self, update_dialog):
        _translate = QtCore.QCoreApplication.translate
        update_dialog.setWindowTitle(_translate("update_dialog", "Dialog"))
        self.update_label.setText(_translate("update_dialog", "<html><head/><body><p>업데이트 중입니다. </p></body></html>"))

