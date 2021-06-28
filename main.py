from gui.total_gui import FinderGUI
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__" :


    app = QApplication(sys.argv)
    word_finder = FinderGUI()
    word_finder.show()
    word_finder.search_word()
    app.exec_()