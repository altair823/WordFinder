import sys
import webbrowser

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from presenter import naver_presenter, wiki_presenter
from gui import finder_gui, update_gui
from core import updater
from core import update_checker
from core.declaration import *

updater_gui = update_gui.Ui_update_dialog

#form_class = uic.loadUiType(os.path.abspath("finder_gui.py"))[0]
finder = finder_gui.Ui_WordFinderGUI


def go_webpage(url):
    webbrowser.open(url)

class Updater_GUI(QDialog, updater_gui):
    def __init__(self, parent):
        super(Updater_GUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Update')
        self.show()
        self.update_thread = QThread()
        self.update_worker = updater.Updater('WordFinder')
        self.update_worker.set_sever(WORDFINDER_FTP_SERVER)
        self.update_worker.set_dir(TEMP_UPDATE_DIR)

        self.update_worker.moveToThread(self.update_thread)
        self.update_thread.started.connect(self.update_worker.update)
        self.update_worker.finished.connect(self.update_thread.quit)
        self.update_worker.finished.connect(self.update_worker.deleteLater)
        self.update_thread.finished.connect(self.update_thread.deleteLater)
        self.update_thread.finished.connect(self.close)
        self.update_thread.start()


class FinderGUI(QMainWindow, finder):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('WordFinder')
        self.word = ''
        self.naver_url = ''
        self.wiki_url = ''
        self.search_bar.returnPressed.connect(self.search_word)
        self.search.clicked.connect(self.search_word)
        self.naver_page.clicked.connect(self.go_naver_page)
        self.wiki_page.clicked.connect(self.go_wiki_page)
        self.update_btn.clicked.connect(self.update)

    def get_word(self):
        return self.search_bar.text()

    def set_word(self, string):
        self.word = string

    def set_naverDict_mean(self, mean_str):
        self.naver_search_result.setText(mean_str)

    def set_wiki_mean(self, mean_str):
        self.wiki_search_result.setText(mean_str)

    def search_word(self):
        target = self.search_bar.text()
        self.set_word(target)
        self.search_bar.clear()

        naver_pre = naver_presenter.NaverPresenter(target)
        wiki_pre = wiki_presenter.WikiPresenter(target)

        naver_mean = naver_pre.get_mean()
        wiki_mean = wiki_pre.get_mean()

        self.naver_url = naver_pre.url
        self.wiki_url = wiki_pre.url

        self.set_naverDict_mean(naver_mean)
        self.set_wiki_mean(wiki_mean)

    def go_naver_page(self):
        webbrowser.open(self.naver_url)

    def go_wiki_page(self):
        webbrowser.open(self.wiki_url)

    def update(self):
        if update_checker.UpdateChecker(RELEASED_FILE_DIR).check() is False:
            print('don\'t needed!')
            return
        updater_g = Updater_GUI(self)
        updater_g.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = FinderGUI()
    myWindow.show()
    app.exec_()