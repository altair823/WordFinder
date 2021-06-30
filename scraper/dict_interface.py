from abc import ABCMeta, abstractmethod


class DictInferface(metaclass=ABCMeta):
    @abstractmethod
    def find(self):
        pass