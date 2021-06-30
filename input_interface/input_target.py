from scraper.naver_dict import NaverDictFinder
from scraper.wikipedia import WikipediaFinder


class WordInput:
    def __init__(self, target):
        self.target = target

    def get_naver_finder(self):
        return NaverDictFinder(self.target)

    def get_wiki_finder(self):
        return WikipediaFinder(self.target)