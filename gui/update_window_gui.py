# 서버와 통신해 프로그램을 업데이트할 때 보이는 창을 구현하는 파일입니다.
# 업데이트 worker를 생성해 파일을 다운로드하고 업데이트 합니다.
# 업데이트 상태를 확인하는 또 다른 worker를 중첩클래스로 생성하여 과정을 progress bar로 시각화합니다.

import os
from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool, QRunnable, pyqtSlot
from PyQt5.QtWidgets import QDialog

from core import updater
from core.declaration import WORDFINDER_FTP_SERVER, TEMP_UPDATE_DIR

# gui 리소스 파일을 참조한다.
from resource.update_window import Ui_update_dialog
updater_gui = Ui_update_dialog


class check_signal(QObject):
    progress = pyqtSignal(int)


class UpdaterGUI(QDialog, updater_gui):
    def __init__(self, parent, filename):
        super(UpdaterGUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Update')
        self.show()
        self.filename = filename
        self.total_size = 0

        # 업데이트하는 worker를 생성한다.
        self.threadpool = QThreadPool()
        self.update_worker = updater.Updater(self.filename)
        self.update_worker.set_sever(WORDFINDER_FTP_SERVER)
        self.update_worker.set_dir(TEMP_UPDATE_DIR)
        self.threadpool.start(self.update_worker)

        # 업데이트 worker가 파일 전체 용량을 가르쳐주면 그때부터 진행상황을 체크한다.
        self.update_worker.signal.total_size.connect(self.check_progress)
        self.update_worker.signal.finished.connect(self.close)

    def check_progress(self, size):
        self.total_size = size
        if self.total_size == 0:
            return

        # 업데이트 진행상황을 체크하는 worker 스레드 클래스.
        class _update_checker(QRunnable):
            def __init__(self, filename, total_size):
                super(_update_checker, self).__init__()
                self.signals = check_signal()
                self.filename = filename
                self.total_size = total_size

            @pyqtSlot()
            def run(self):
                current_size = 0
                total = self.total_size
                sleep(3)
                # 업데이트 진행상황을 일정한 간격으로 체크한다.
                while (current_size <= total):
                    if os.path.isfile(os.path.join(TEMP_UPDATE_DIR, self.filename + '.zip')):
                        current_size = os.path.getsize(os.path.join(TEMP_UPDATE_DIR, self.filename + '.zip'))
                    else:
                        return
                    self.signals.progress.emit((int(current_size) / total) * 100)
                    sleep(0.01)

        self.progress_checker = _update_checker(self.filename, self.total_size)
        self.threadpool.start(self.progress_checker)
        self.progress_checker.signals.progress.connect(self.progress_bar.setValue)
