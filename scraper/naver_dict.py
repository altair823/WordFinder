import urllib
import requests


class NaverDictFinder:
    def __init__(self, target):
        if target is None:
            self.target = ''
        else:
            self.target = urllib.parse.quote(target)
        self.request = None
        self.url = ''
        self.result = None

        try:
            self.url = "https://dict.naver.com/search.dict?dicQuery=" + self.target
            self.request = requests.get(self.url, timeout=2)
        except requests.exceptions.ConnectTimeout:
            self.url = ''
            self.result = ''
