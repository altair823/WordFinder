import ftplib
import os
import shutil
import threading
import platform
from time import sleep
from zipfile import ZipFile
from PyQt5.QtCore import QObject, pyqtSignal
from file_extension import FileName
import update_gui


# Temporary directory that will contains downloaded files which is replaced the original files.
# And the old files will moving this temp_dir.
temp_update_dir = 'tmp_update'


# Downloader that download updating files by ftp protocol.
class Downloader(threading.Thread):
    # Argument named 'is_complete' is the flag representing the downloading sequence complete.
    def __init__(self, exit_flag):
        super().__init__()
        self.server = ''
        self.filename = None
        self.exit_flag = exit_flag

    def setServer(self, server):
        self.server = server

    def setFilename(self, filename):
        # Type check the filename argument.
        if type(filename) is str:
            self.filename = FileName(filename)
        elif type(filename) is FileName:
            self.filename = filename
        else:
            raise Exception('wrong filename type')

    # For multithreading.
    def run(self):
        # If temp_dir exist, delete it and make a new one.
        if os.path.isdir(temp_update_dir) is True:
            shutil.rmtree(temp_update_dir)
        os.makedirs(temp_update_dir)

        def file_write(data):
            file.write(data)
        try:
            # Download files by ftp protocol in certain thread.
            ftp = ftplib.FTP(self.server)
            # Anonymous login.
            ftp.login()
            ftp.cwd('Released_files')
            #file_size = ftp.size(self.filename.zip)
            # Download files to temp_dir.
            file = open(os.path.join(temp_update_dir, self.filename.zip), 'wb')
            ftp.retrbinary('RETR ' + self.filename.zip, file_write)
        except Exception as e:
            print('Failed to download from ftp server.', e)
            print('Abort program')
            raise
            # There must be new window alarm for exceptions.
        self.exit_flag['filename'] = self.filename
        # Move downloaded file to temp_dir
        # shutil.move(self.filename.filename_zip, os.path.join(_TMP_DIR, self.filename.filename_zip))


class Updater(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    # The given filename must be without extension.
    def __init__(self, filename_without_extension):
        super().__init__()
        self.server = '61.73.209.90'
        self.filename = FileName(filename_without_extension)
        self.exit_flag = False


    def update(self):
        try:
            res = {}
            d = Downloader(res)
            d.setDaemon(True)
            d.setServer(self.server)
            d.setFilename(self.filename)
            d.start()
        # If update sequence cannot be executed,
        except Exception as e:
            del d
            raise
        else:
            while 'filename' not in res:
                sleep(1)
            del d
            if res['filename'] is None:
                raise Exception('Failed to download')

            with ZipFile(os.path.join(temp_update_dir, self.filename.zip)) as zip:
                zip.extractall(temp_update_dir)
            os.remove(os.path.join(temp_update_dir, self.filename.zip))

            move_old_and_new(self.filename)
            start_new(self.filename)
            self.exit_flag = True
            exit(0)

    def is_finished(self):
        return self.exit_flag

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


