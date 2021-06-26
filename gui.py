import sys
import os
import webbrowser

from PyQt5.QtWidgets import *
from PyQt5 import uic
from wikipedia import WikipediaFinder
from naver_dict import NaverDictFinder
import finder_gui


#form_class = uic.loadUiType(os.path.abspath("finder_gui.py"))[0]
form_class = finder_gui.Ui_WordFinderGUI


def go_webpage(url):
    webbrowser.open(url)


class FinderGUI(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.word = ''
        self.naver_url = ''
        self.wiki_url = ''
        self.search_bar.returnPressed.connect(self.search_word)
        self.search.clicked.connect(self.search_word)
        self.naver_page.clicked.connect(self.go_naver_page)
        self.wiki_page.clicked.connect(self.go_wiki_page)

    def get_word(self):
        return self.search_bar.text()

    def set_word(self, string):
        self.word = string

    def set_naverDict_mean(self, mean_str):
        self.naver_search_result.setText(mean_str)

    def set_wiki_mean(self, mean_str):
        self.wiki_search_result.setText(mean_str)

    def search_word(self):
        a = self.search_bar.text()
        self.set_word(a)
        self.search_bar.clear()
        naver_dict = NaverDictFinder(self.word)
        wiki = WikipediaFinder(self.word)
        naver_mean = naver_dict.find()
        wiki_mean = wiki.find()
        self.naver_url = naver_dict.url
        self.wiki_url = wiki.url
        self.set_naverDict_mean(naver_mean)
        self.set_wiki_mean(wiki_mean)

    def go_naver_page(self):
        webbrowser.open(self.naver_url)

    def go_wiki_page(self):
        webbrowser.open(self.wiki_url)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = FinderGUI()
    myWindow.show()
    app.exec_()