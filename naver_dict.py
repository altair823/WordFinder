import requests
from bs4 import BeautifulSoup


class NaverDictFinder:
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
            self.url = requests.get("https://dict.naver.com/search.dict?dicQuery=" + self.target, timeout=2)
            soup = BeautifulSoup(self.url.text, 'lxml')
            #print(soup)
            self.result = soup.find(class_='lst_krdic')
        except requests.exceptions.ConnectTimeout:
            return []
        else:
            if self.result is None:
                return ''
            extracted_str = self.result.text.replace('\t', '').replace('\r', '').split('\n')
            extracted_str = [v for v in extracted_str if v and not 'play' in v]

            return '\n'.join(extracted_str)