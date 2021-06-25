import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from wikipedia import WikipediaFinder
from naver_dict import NaverDictFinder

form_class = uic.loadUiType(os.path.abspath("bus_gui.ui"))[0]


class FinderGUI(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.word = ''
        self.search_bar.returnPressed.connect(self.search_word)
        self.search.clicked.connect(self.search_word)

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
        if a != '':
            print(a)
            self.set_word(a)
            self.search_bar.clear()
            naver_dict = NaverDictFinder(self.word)
            wiki = WikipediaFinder(self.word)
            naver_mean = naver_dict.find()
            wiki_mean = wiki.find()
            self.set_naverDict_mean(naver_mean)
            self.set_wiki_mean(wiki_mean)
        else:
            print("eqffqef")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = FinderGUI()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()