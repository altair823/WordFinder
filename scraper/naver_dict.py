import urllib
import requests
from scraper.finder_interface import _FinderInterface


class NaverDictFinder(_FinderInterface):
    def __init__(self, target):
        if target is None:
            self.target = ''
        else:
            self.target = urllib.parse.quote(target)
        self.request = None
        self.url = ''

        try:
            self.url = "https://dict.naver.com/search.dict?dicQuery=" + self.target
            self.request = requests.get(self.url, timeout=2)
        except requests.exceptions.ConnectTimeout:
            self.url = ''

    def get_url(self):
        return self.url

    def get_text(self):
        if self.request is None:
            return ''
        return self.request.text