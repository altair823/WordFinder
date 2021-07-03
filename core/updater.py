import os
import shutil
import platform
from zipfile import ZipFile
from PyQt5.QtCore import QObject, pyqtSignal, QThread, QRunnable, pyqtSlot

from core.declaration import IS_THIS_TEST
from core.downloader import Downloader, rm_update_dir
from core.file_extension import FileName


class _UpdaterSignal(QObject):
    finished = pyqtSignal()
    total_size = pyqtSignal(int)


class Updater(QRunnable):

    # The given filename must be without extension.
    def __init__(self, filename_without_extension):
        super().__init__()
        self.signal = _UpdaterSignal()

        self.server = None
        self.filename = FileName(filename_without_extension)
        self.downloader = None
        self.temp_update_dir = None

    def set_sever(self, server):
        self.server = server

    def set_dir(self, temp_dir):
        self.temp_update_dir = temp_dir

    def update(self):
        try:
            # Download updated file.
            self.downloader = Downloader()
            self.downloader.setServer(self.server)
            self.downloader.setFilename(self.filename)
            self.downloader.login()
            total_size = self.downloader.get_size()
            self.signal.total_size.emit(total_size)
            self.downloader.download()
            del self.downloader
        # If update sequence cannot be executed,
        except Exception as e:
            raise
        else:
            # Unzip downloaded file which is newer.
            with ZipFile(os.path.join(self.temp_update_dir, self.filename.zip)) as zip:
                zip.extractall(self.temp_update_dir)
            os.remove(os.path.join(self.temp_update_dir, self.filename.zip))

            try:
                self.move_old_start_new(self.filename)
            except Exception:
                print('플랫폼 이슈!')
                rm_update_dir()
                exit(1)

    # Move the old file to temp_update_dir
    # And move the new downloaded files to current directory.
    # If anything exist in temp_update_dir, they will be moved to current dir.
    # All tasks are done, start new .exe.
    def move_old_start_new(self, filename):
        current_path = os.path.basename(filename.exe)
        new_files = os.listdir(self.temp_update_dir)
        name_old = os.path.join(self.temp_update_dir, '{}_old'.format(current_path))
        if os.path.exists(name_old):
            os.remove(name_old)
        if os.path.exists(current_path):
            os.rename(current_path, name_old)
        for file in new_files:
            if file[3:] != 'old':
                shutil.move(os.path.join(self.temp_update_dir, file), file)
        os.rename(filename.exe, current_path)

        if IS_THIS_TEST is False:
            if platform.system() == 'Windows':
                os.startfile(filename.exe)
                exit(0)
            else:
                raise Exception("지원되지 않는 플랫폼입니다")
        else:
            print('테스트 환경입니다.')

    @pyqtSlot()
    def run(self):
        self.update()
        self.signal.finished.emit()
