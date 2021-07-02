import sys
import webbrowser

from PyQt5.QtCore import QThread, QObject, QThreadPool, pyqtSignal, pyqtSlot, QRunnable
from PyQt5.QtWidgets import *
from presenter import naver_presenter, wiki_presenter
from gui import finder_gui, update_gui
from core import updater
from core import update_checker
from core.declaration import *

from input_interface.input_target import WordInput
from scraper import naver_dict, wikipedia

updater_gui = update_gui.Ui_update_dialog
finder = finder_gui.Ui_WordFinderGUI


def go_webpage(url):
    webbrowser.open(url)

class Updater_GUI(QDialog, updater_gui):
    def __init__(self, parent):
        super(Updater_GUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Update')
        self.show()
        self.update_worker = updater.Updater('WordFinder')
        self.update_worker.set_sever(WORDFINDER_FTP_SERVER)
        self.update_worker.set_dir(TEMP_UPDATE_DIR)

        self.update_worker.start()
        self.update_worker.finished.connect(self.close)

class WorkerSignals(QObject):
    result = pyqtSignal(str)
    finished = pyqtSignal()

class NaverThreadFinder(QRunnable):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        navar_pre = naver_presenter.NaverPresenter()
        navar_result = navar_pre.present_mean(WordInput(self.target).get_naver_finder().request.text)
        self.signals.result.emit(navar_result)
        self.signals.finished.emit()


class WikiThreadFinder(QRunnable):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        wiki_pre = wiki_presenter.WikiPresenter()
        wiki_result = wiki_pre.present_mean(WordInput(self.target).get_wiki_finder().request.text)
        self.signals.result.emit(wiki_result)
        self.signals.finished.emit()


class FinderGUI(QMainWindow, finder):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Word Finder')
        self.version_indicator.setText('version ' + CURRENT_VERSION)
        self.word = ''
        self.naver_url = ''
        self.wiki_url = ''
        self.search_bar.returnPressed.connect(self.search_word)
        self.search.clicked.connect(self.search_word)
        self.naver_page.clicked.connect(self.go_naver_page)
        self.wiki_page.clicked.connect(self.go_wiki_page)
        self.update_btn.clicked.connect(self.update)

        self.threadpool = QThreadPool()

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

        naver_finder = NaverThreadFinder(target)
        naver_finder.signals.result.connect(self.set_naverDict_mean)
        self.threadpool.start(naver_finder)

        wiki_finder = WikiThreadFinder(target)
        naver_finder.signals.result.connect(self.set_wiki_mean)
        self.threadpool.start(wiki_finder)


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