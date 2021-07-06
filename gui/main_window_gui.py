# 메인 윈도우를 구현하는 파일입니다.
import webbrowser

from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import *

from gui.update_window_gui import UpdaterGUI
from gui.help_window_gui import HelpWindow
from multithread import wiki_thread_finder, naver_thread_finder
from resource.main_window import Ui_MainWindow
from core import update_checker, file_manage
from core.declaration import *



class FinderGUI(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Word Finder')

        self.menu_file_save.triggered.connect(self.save_file)
        self.menu_file_open.triggered.connect(self.open_file)

        self.menu_info_update.triggered.connect(self.update)
        self.menu_info_program_ver.triggered.connect(self.show_version)
        self.menu_info_help.triggered.connect(self.show_help)

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
        naver_finder = naver_thread_finder.NaverThreadFinder(self.target)
        naver_finder.signals.result.connect(self.set_naverDict_mean)

        # 위키백과 탐색
        wiki_finder = wiki_thread_finder.WikiThreadFinder(self.target)
        wiki_finder.signals.result.connect(self.set_wiki_mean)

        # Start thread
        self.threadpool.start(naver_finder)
        self.threadpool.start(wiki_finder)

    def go_naver_page(self):
        webbrowser.open(self.naver_url)

    def go_wiki_page(self):
        webbrowser.open(self.wiki_url)

    # Save current search result by text file.
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, '저장', '', 'Text (*.txt);;' 'All Files (*.*)')
        if filename:
            save_data = file_manage.FileManager()
            save_data.add_mean('naver_dict', self.naver_result.text())
            save_data.add_mean('wikipedia', self.wiki_result.text())
            save_data.save_text(filename)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, '열기', '', 'Text (*.txt);;' 'All Files (*.*)')
        if filename:
            open_data = file_manage.FileManager()
            data = open_data.load_text(filename)
            self.naver_result.setText(data['naver_dict'])
            self.wiki_result.setText(data['wikipedia'])

    def update(self):
        # 현재 버전과 서버의 버전을 체크하고 필요할 경우에만 업데이트.
        if update_checker.UpdateChecker(RELEASED_FILE_DIR).check() is False:
            print('don\'t needed!')
            return
        updater_g = UpdaterGUI(self, 'WordFinder')
        updater_g.show()

    def show_version(self):
        version_window = QMessageBox(self)
        version_window.setWindowTitle('About')
        version_window.setIcon(QMessageBox.Information)
        version_window.setText('Currnet version is ' + CURRENT_VERSION)
        version_window.exec_()

    def show_help(self):
        help_g = HelpWindow(self)
        help_g.show()

