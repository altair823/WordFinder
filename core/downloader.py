import ftplib
import os
import shutil

from core.declaration import TEMP_UPDATE_DIR
from core.file_extension import FileName


# Remove if there is update_dir existing.
def rm_update_dir():
    if os.path.isdir(TEMP_UPDATE_DIR) is True:
        shutil.rmtree(TEMP_UPDATE_DIR)

# If update_dir exist, delete it and make a new one.
def mk_update_dir():
    if os.path.isdir(TEMP_UPDATE_DIR) is True:
        shutil.rmtree(TEMP_UPDATE_DIR)
    os.makedirs(TEMP_UPDATE_DIR)


# Downloader that download updating files by ftp protocol.
class Downloader:
    # Argument named 'is_complete' is the flag representing the downloading sequence complete.
    def __init__(self):
        super().__init__()
        self.server = ''
        self.filename = None
        self.ftp = None

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

    def login(self):
        try:
            # Download files by ftp protocol in certain thread.
            self.ftp = ftplib.FTP(self.server)
            # Anonymous login.
            self.ftp.login()
            self.ftp.cwd('Released_files')
        except Exception as e:
            print('Failed to download from ftp server.', e)
            print('Abort program')
            raise

    def get_size(self):
        self.ftp.voidcmd('TYPE I')
        return self.ftp.size(self.filename.zip)

    def download(self):
        mk_update_dir()

        def file_write(data):
            file.write(data)
        try:
            # Download files to temp_dir.
            file = open(os.path.join(TEMP_UPDATE_DIR, self.filename.zip), 'wb')
            self.ftp.retrbinary('RETR ' + self.filename.zip, file_write)
            file.close()
        except Exception as e:
            print('Failed to download from ftp server.', e)
            print('Abort program')
            raise
            # There must be new window alarm for exceptions.

    def __del__(self):
        if self.ftp is not None:
            self.ftp.close()

    def abort_ftp_download(self):
        if self.ftp is not None and type(self.ftp) is ftplib.FTP:
            self.ftp.abort()

