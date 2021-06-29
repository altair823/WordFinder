import presenter.word_presenter_interface
from scraper.naver_dict import NaverDictFinder


class NaverPresenter(presenter.word_presenter_interface.WordPresenter):
    def __init__(self, target):
        self.target = target
        self.url = None

    def get_mean(self):
        naver_finder = NaverDictFinder(self.target)
        self.url = naver_finder.url
        return naver_finder.find()
