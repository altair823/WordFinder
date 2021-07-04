from PyQt5.QtCore import QRunnable, pyqtSlot
from multithread.thread_signals import WorkerSignals
from presenter import wiki_presenter
from scraper import wikipedia


class WikiThreadFinder(QRunnable):
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
            wiki_pre = wiki_presenter.WikiPresenter()
            wiki_finder = wikipedia.WikipediaFinder(self.target)
            wiki_result = dict()
            wiki_result['url'] = wiki_finder.get_url()
            wiki_result['text'] = wiki_pre.present_mean(wiki_finder.get_text())
            self.signals.result.emit(wiki_result)
            self.signals.finished.emit()