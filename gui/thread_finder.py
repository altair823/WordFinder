# Finder 객체와 Presenter 객체를 받아 target을 해당 페이지에서 검색한 결과를 반환하는 스레드 기반 검색 클래스입니다.
# Finder 객체는 scraper.finder_interface의 _FinderInterface를 상속받은 객체여야 합니다.

from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal


class WorkerSignals(QObject):
    result = pyqtSignal(dict)
    finished = pyqtSignal()


class ThreadFinder(QRunnable):
    def __init__(self):
        super().__init__()
        self.target = None
        self.signals = WorkerSignals()
        self.finder = None
        self.presenter = None

    def set_target(self, target):
        self.target = target

    # Use generics to set finder and presenter.
    def set_finder(self, finder):
        self.finder = finder

    def set_presenter(self, presenter):
        self.presenter = presenter

    @pyqtSlot()
    def run(self):
        if self.target == '':
            # Result must be a dictionary that contains the url and text of target html.
            self.signals.result.emit({'url': '', 'text': ''})
            self.signals.finished.emit()
        else:
            naver_result = dict()
            naver_result['url'] = self.finder.get_url()
            naver_result['text'] = self.presenter.present_mean(self.finder.get_text())
            self.signals.result.emit(naver_result)
            self.signals.finished.emit()