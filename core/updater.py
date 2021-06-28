import shutil
import platform
from time import sleep
from zipfile import ZipFile
from PyQt5.QtCore import QObject, pyqtSignal

from core.declaration import WORDFINDER_FTP_SERVER
from core.downloader import Downloader
from file_extension import FileName


class Updater(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    # The given filename must be without extension.
    def __init__(self, filename_without_extension):
        super().__init__()
        self.server = WORDFINDER_FTP_SERVER
        self.filename = FileName(filename_without_extension)
        self.downloader = None


    def update(self):
        try:
            res = {}
            self.downloader = Downloader(res)
            self.downloader.setServer(self.server)
            self.downloader.setFilename(self.filename)
            #self.d.setDaemon(True)
            self.downloader.run()
        # If update sequence cannot be executed,
        except Exception as e:
            raise
        else:
            while 'filename' not in res:
                sleep(1)
            if res['filename'] is None:
                raise Exception('Failed to download')

            with ZipFile(os.path.join(temp_update_dir, self.filename.zip)) as zip:
                zip.extractall(temp_update_dir)
            os.remove(os.path.join(temp_update_dir, self.filename.zip))

            move_old_and_new(self.filename)
            try:
                start_new(self.filename)
            except Exception:
                print('플랫폼 이슈!')
                exit(1)


# Move the old file to temp_update_dir
# And move the new downloaded files to current directory.
# If anything exist in temp_update_dir, they will be moved to current dir.
def move_old_and_new(filename):
    current_path = os.path.basename(filename.exe)
    new_files = os.listdir(temp_update_dir)
    name_old = os.path.join(temp_update_dir, '{}_old'.format(current_path))
    if os.path.exists(name_old):
        os.remove(name_old)
    if os.path.exists(current_path):
        os.rename(current_path, name_old)
    for file in new_files:
        if file[3:] != 'old':
            shutil.move(os.path.join(temp_update_dir, file), file)
    os.rename(filename.exe, current_path)

def start_new(filename):
    # Execute file if the os is Windows.
    if platform.system() == 'Windows':
        os.startfile(os.path.basename(filename.exe))
        exit(0)
    #else:
    #    raise Exception("지원되지 않는 플랫폼입니다")

