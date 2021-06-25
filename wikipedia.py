import requests
from bs4 import BeautifulSoup


class WikipediaFinder:
    def __init__(self, target):
        if target is None:
            print("3r3r")
            self.target = ''
        else:
            self.target = target
        self.url = ''
        self.result = None

    def find(self):
        try:
            self.url = requests.get("https://ko.wikipedia.org/wiki/" + self.target, timeout=2)
            soup = BeautifulSoup(self.url.text, 'lxml')
            self.result = soup.find_all('p')
        except requests.exceptions.ConnectTimeout:
            return []
        else:
            if self.result is None:
                return ''
            extracted_str = [v.text.replace('\t', '').replace('\r', '') for v in self.result]
            extracted_str = [v.strip('\n') for v in extracted_str if v != '\n']
            return '\n'.join(extracted_str)
