import ftplib
import os
import shutil
import threading

from core.declaration import temp_update_dir
from file_extension import FileName


# Remove if there is update_dir existing.
def rm_update_dir():
    if os.path.isdir(temp_update_dir) is True:
        shutil.rmtree(temp_update_dir)

# If update_dir exist, delete it and make a new one.
def mk_update_dir():
    if os.path.isdir(temp_update_dir) is True:
        shutil.rmtree(temp_update_dir)
    os.makedirs(temp_update_dir)


# Downloader that download updating files by ftp protocol.
class Downloader:
    # Argument named 'is_complete' is the flag representing the downloading sequence complete.
    def __init__(self, res):
        super().__init__()
        self.server = ''
        self.filename = None
        self.ftp = None
        self.res = res

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

    def download(self):
        mk_update_dir()

        def file_write(data):
            file.write(data)
        try:
            # Download files by ftp protocol in certain thread.
            self.ftp = ftplib.FTP(self.server)
            # Anonymous login.
            self.ftp.login()
            self.ftp.cwd('Released_files')
            #file_size = ftp.size(self.filename.zip)
            # Download files to temp_dir.
            file = open(os.path.join(temp_update_dir, self.filename.zip), 'wb')
            self.ftp.retrbinary('RETR ' + self.filename.zip, file_write)
            file.close()
        except Exception as e:
            print('Failed to download from ftp server.', e)
            print('Abort program')
            raise
            # There must be new window alarm for exceptions.
        else:
            self.res['filename'] = file
            self.ftp.close()

    def abort_ftp_download(self):
        if self.ftp is not None and type(self.ftp) is ftplib.FTP:
            self.ftp.abort()

