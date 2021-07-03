import sys
import webbrowser
from time import sleep

from PyQt5.QtCore import QThread, QObject, QThreadPool, pyqtSignal, pyqtSlot, QRunnable
from PyQt5.QtWidgets import *
from presenter import naver_presenter, wiki_presenter
from gui import main_window, update_gui
from core import updater
from core import update_checker
from core.declaration import *

from input_interface.input_target import WordInput
from scraper import naver_dict, wikipedia

updater_gui = update_gui.Ui_update_dialog
finder = main_window.Ui_MainWindow


class check_signal(QObject):
    progress = pyqtSignal(int)

class Updater_GUI(QDialog, updater_gui):
    def __init__(self, parent, filename):
        super(Updater_GUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Update')
        self.show()
        self.filename = filename
        self.total_size = 0
        self.threadpool = QThreadPool()
        self.update_worker = updater.Updater(self.filename)
        self.update_worker.set_sever(WORDFINDER_FTP_SERVER)
        self.update_worker.set_dir(TEMP_UPDATE_DIR)
        self.threadpool.start(self.update_worker)

        self.update_worker.signal.total_size.connect(self.set_total_size)
        self.update_worker.signal.finished.connect(self.close)

    def set_total_size(self, size):
        self.total_size = size
        if self.total_size == 0:
            return

        class _update_checker(QRunnable):
            def __init__(self, filename, total_size):
                super(_update_checker, self).__init__()
                self.signals = check_signal()
                self.filename = filename
                self.total_size = total_size

            @pyqtSlot()
            def run(self):
                current_size = 0
                total = self.total_size
                while (current_size <= total):
                    if os.path.isfile(os.path.join(TEMP_UPDATE_DIR, self.filename + '.zip')):
                        current_size = os.path.getsize(os.path.join(TEMP_UPDATE_DIR, self.filename + '.zip'))
                    else:
                        return
                    self.signals.progress.emit((int(current_size) / total) * 100)
                    sleep(1)

        self.progress_checker = _update_checker(self.filename, self.total_size)
        self.threadpool.start(self.progress_checker)
        self.progress_checker.signals.progress.connect(self.progress_check)

    def progress_check(self, progress):
        self.progress_bar.setValue(progress)


class WorkerSignals(QObject):
    result = pyqtSignal(dict)
    finished = pyqtSignal()

class NaverThreadFinder(QRunnable):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        if self.target == '':
            self.signals.result.emit({'url': '', 'text': ''})
            self.signals.finished.emit()
        else:
            navar_pre = naver_presenter.NaverPresenter()
            naver_finder = WordInput(self.target).get_naver_finder()
            naver_result = dict()
            naver_result['url'] = naver_finder.url
            naver_result['text'] = navar_pre.present_mean(naver_finder.request.text)
            self.signals.result.emit(naver_result)
            self.signals.finished.emit()


class WikiThreadFinder(QRunnable):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        if self.target == '':
            self.signals.result.emit({'url': '', 'text': ''})
            self.signals.finished.emit()
        else:
            wiki_pre = wiki_presenter.WikiPresenter()
            wiki_finder = WordInput(self.target).get_wiki_finder()
            wiki_result = dict()
            wiki_result['url'] = wiki_finder.url
            wiki_result['text'] = wiki_pre.present_mean(wiki_finder.request.text)
            self.signals.result.emit(wiki_result)
            self.signals.finished.emit()


class FinderGUI(QMainWindow, finder):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Word Finder')

        self.menu_info_update.triggered.connect(self.update)

        self.word = ''
        self.naver_url = ''
        self.wiki_url = ''
        self.search_bar.returnPressed.connect(self.search_word)
        self.search_button.clicked.connect(self.search_word)
        self.naver_gopage.clicked.connect(self.go_naver_page)
        self.wiki_gopage.clicked.connect(self.go_wiki_page)

        self.threadpool = QThreadPool()

    def get_word(self):
        return self.search_bar.text()

    def set_word(self, string):
        self.word = string

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
        target = self.search_bar.text()
        self.set_word(target)
        self.search_bar.clear()

        naver_finder = NaverThreadFinder(target)
        naver_finder.signals.result.connect(self.set_naverDict_mean)
        self.threadpool.start(naver_finder)

        wiki_finder = WikiThreadFinder(target)
        wiki_finder.signals.result.connect(self.set_wiki_mean)
        self.threadpool.start(wiki_finder)


    def go_naver_page(self):
        webbrowser.open(self.naver_url)

    def go_wiki_page(self):
        webbrowser.open(self.wiki_url)

    def update(self):
        if update_checker.UpdateChecker(RELEASED_FILE_DIR).check() is False:
            print('don\'t needed!')
            return
        updater_g = Updater_GUI(self, 'WordFinder')
        updater_g.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = FinderGUI()
    myWindow.show()
    app.exec_()