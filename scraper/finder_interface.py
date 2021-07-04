from abc import ABCMeta, abstractmethod


class _FinderInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def get_url(self):
        pass