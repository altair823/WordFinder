import urllib
import requests


class WikipediaFinder:
    def __init__(self, target):
        if target is None:
            self.target = ''
        else:
            self.target = urllib.parse.quote(target)
        self.request = None
        self.url = ''
        self.result = None
        try:
            self.url = "https://ko.wikipedia.org/wiki/" + self.target
            self.request = requests.get(self.url, timeout=2)
        except requests.exceptions.ConnectTimeout:
            self.url = ''
            self.result = ''
