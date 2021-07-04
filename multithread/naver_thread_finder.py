from PyQt5.QtCore import QRunnable, pyqtSlot
from multithread.thread_signals import WorkerSignals
from presenter import naver_presenter
from scraper import naver_dict


class NaverThreadFinder(QRunnable):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        if self.target == '':
            # Result must be a dictionary that contains the url and text of target html.
            self.signals.result.emit({'url': '', 'text': ''})
            self.signals.finished.emit()
        else:
            naver_pre = naver_presenter.NaverPresenter()
            naver_finder = naver_dict.NaverDictFinder(self.target)
            naver_result = dict()
            naver_result['url'] = naver_finder.get_url()
            naver_result['text'] = naver_pre.present_mean(naver_finder.get_text())
            self.signals.result.emit(naver_result)
            self.signals.finished.emit()