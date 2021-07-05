import os
from ftplib import FTP
from core.declaration import *
from core.downloader import mk_update_dir


# This class download help file for using program from the certain ftp server.
class HelpDownloader:
    def __init__(self):
        self.server = None

    def set_server(self, server):
        self.server = server

    def download(self, filename):
        if self.server is None:
            raise Exception('No server exception!')
        try:
            # Make temp dir if there is no such folder.
            mk_update_dir()

            ftp = FTP(self.server)
            ftp.login()
            ftp.cwd('Released_files')
            file = open(os.path.join(TEMP_UPDATE_DIR, filename), 'wb')
            ftp.retrbinary('RETR ' + filename.zip, file.write)
            file.close()
        except Exception as e:
            print('Failed to download from ftp server.', e)
            raise


def remove_help(filename):
    if os.path.isdir(TEMP_UPDATE_DIR) is True:
        try:
            os.remove(os.path.join(TEMP_UPDATE_DIR, filename))
        except FileNotFoundError as e:
            pass
