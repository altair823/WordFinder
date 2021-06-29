from abc import ABCMeta, abstractmethod


class WordPresenter(metaclass=ABCMeta):
    target = ''
    url = ''
    @abstractmethod
    def get_mean(self):
        pass


