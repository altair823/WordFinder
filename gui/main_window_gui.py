# 메인 윈도우를 구현하는 파일입니다.

import sys
import webbrowser

from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import *

from gui.update_window_gui import Updater_GUI
from presenter import naver_presenter, wiki_presenter
from gui import thread_finder
from resource.main_window import Ui_MainWindow
from core import update_checker
from core.declaration import *
from scraper import naver_dict, wikipedia


finder = Ui_MainWindow


class FinderGUI(QMainWindow, finder):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Word Finder')

        self.menu_info_update.triggered.connect(self.update)

        self.target = ''
        self.naver_url = ''
        self.wiki_url = ''
        self.search_bar.returnPressed.connect(self.search_word)
        self.search_button.clicked.connect(self.search_word)
        self.naver_gopage.clicked.connect(self.go_naver_page)
        self.wiki_gopage.clicked.connect(self.go_wiki_page)

        # 각 사이트의 결과를 탐색할 스레드가 존재할 스래드풀.
        self.threadpool = QThreadPool()

    def set_naverDict_mean(self, result_dict):
        for key in result_dict.keys():
            if key == 'url':
                self.naver_url = result_dict[key]
            if key == 'text':
                self.naver_result.setText(result_dict[key])

    def set_wiki_mean(self, result_dict):
        for key in result_dict.keys():
            if key == 'url':
                self.wiki_url = result_dict[key]
            if key == 'text':
                self.wiki_result.setText(result_dict[key])

    def search_word(self):
        self.target = self.search_bar.text()
        self.search_bar.clear()

        # 네이버 사전 탐색
        naver_finder = thread_finder.ThreadFinder()
        naver_finder.set_target(self.target)
        naver_finder.set_finder(naver_dict.NaverDictFinder(self.target))
        naver_finder.set_presenter(naver_presenter.NaverPresenter())
        naver_finder.signals.result.connect(self.set_naverDict_mean)

        # 위키백과 탐색
        wiki_finder = thread_finder.ThreadFinder()
        wiki_finder.set_target(self.target)
        wiki_finder.set_finder(wikipedia.WikipediaFinder(self.target))
        wiki_finder.set_presenter(wiki_presenter.WikiPresenter())
        wiki_finder.signals.result.connect(self.set_wiki_mean)

        self.threadpool.start(naver_finder)
        self.threadpool.start(wiki_finder)

    def go_naver_page(self):
        webbrowser.open(self.naver_url)

    def go_wiki_page(self):
        webbrowser.open(self.wiki_url)

    def update(self):
        # 현재 버전과 서버의 버전을 체크하고 필요할 경우에만 업데이트.
        if update_checker.UpdateChecker(RELEASED_FILE_DIR).check() is False:
            print('don\'t needed!')
            return
        updater_g = Updater_GUI(self, 'WordFinder')
        updater_g.show()
