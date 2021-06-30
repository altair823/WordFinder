from abc import ABCMeta, abstractmethod


class WordPresenter(metaclass=ABCMeta):
    target = ''
    url = ''
    @abstractmethod
    def present_mean(self, mean):
        pass

    @abstractmethod
    def present_url(self, url):
        pass


