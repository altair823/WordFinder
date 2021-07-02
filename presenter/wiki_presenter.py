from bs4 import BeautifulSoup

import presenter.word_presenter_interface
from scraper.wikipedia import WikipediaFinder


class WikiPresenter(presenter.word_presenter_interface.WordPresenter):

    def present_mean(self, mean):
        soup = BeautifulSoup(mean, 'lxml')
        result = soup.find_all(['p'])

        if result is None:
            return ''

        extracted_str = [v.text.replace('\t', '').replace('\r', '') for v in result]
        extracted_str = [v.strip('\n') for v in extracted_str if v != '\n']

        return '\n'.join(extracted_str)

    def present_url(self, url):
        return url

    def web_html_test(self, html):
        return html