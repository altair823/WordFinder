import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QFrame, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTimer


class MainWindow(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(MainWindow, self).__init__()

        self.button = QPushButton('Show/Hide')
        self.button.setCheckable(True)
        self.frame = QFrame()
        self.frame.setFixedHeight(100)
        self.layout = layout = QVBoxLayout()
        layout2 = QVBoxLayout()
        self.setLayout(layout)
        self.frame.setLayout(layout2)

        layout.addWidget(self.button)
        layout.addWidget(self.frame)
        layout.addStretch(1)
        layout2.addWidget(QLabel('Yoyoyo'))

        self.button.toggled.connect(self.clickAction)

    def startup(self):
        self.show()
        sys.exit(self.app.exec_())

    def clickAction(self):
        checked = self.button.isChecked()
        if checked:
            self.frame.show()
        else:
            self.frame.hide()
        QTimer.singleShot(0, self.resizeMe)

    def resizeMe(self):
        self.resize(self.minimumSizeHint())
if __name__ == "__main__":
    myApp = MainWindow()
    myApp.startup()