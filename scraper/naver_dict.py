import urllib
import requests
import scraper.dict_interface


class NaverDictFinder(scraper.dict_interface.DictInferface):
    def __init__(self, target):
        if target is None:
            self.target = ''
        else:
            self.target = urllib.parse.quote(target)
        self.request = None
        self.url = ''
        self.result = None

    def find(self):
        try:
            self.url = "https://dict.naver.com/search.dict?dicQuery=" + self.target
            self.request = requests.get(self.url, timeout=2)
        except requests.exceptions.ConnectTimeout:
            return []
        else:
            return self.request.text