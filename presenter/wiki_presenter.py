import presenter.word_presenter_interface
from scraper.wikipedia import WikipediaFinder


class WikiPresenter(presenter.word_presenter_interface.WordPresenter):
    def __init__(self, target):
        self.target = target
        self.url = None

    def get_mean(self):
        wiki_finder = WikipediaFinder(self.target)
        self.url = wiki_finder.url
        return wiki_finder.find()