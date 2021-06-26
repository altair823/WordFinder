import webbrowser

from wikipedia import WikipediaFinder
from naver_dict import NaverDictFinder
from gui import FinderGUI
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEventLoop
import sys


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    word_finder = FinderGUI()
    word_finder.show()
    word_finder.search_word()
    app.exec_()