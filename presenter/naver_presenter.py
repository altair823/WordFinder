# Presenter for naver dictionary result page's html.
from bs4 import BeautifulSoup

import presenter.word_presenter_interface


class NaverPresenter(presenter.word_presenter_interface.WordPresenter):

    def present_mean(self, mean):
        soup = BeautifulSoup(mean, 'lxml')
        result = soup.find(class_='lst_krdic')

        if result is None:
            return ''

        extracted_str = result.text.replace('\t', '').replace('\r', '').split('\n')
        extracted_str = [v for v in extracted_str if v and not 'play' in v]

        return '\n'.join(extracted_str)

    def present_url(self, url):
        return url

    def web_html_test(self, html):
        return html
