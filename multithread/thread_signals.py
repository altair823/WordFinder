# Signals for finder threads.

from PyQt5.QtCore import QObject, pyqtSignal


class WorkerSignals(QObject):
    result = pyqtSignal(dict)
    finished = pyqtSignal()
