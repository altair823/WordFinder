import os
from ftplib import FTP
from core.declaration import *
from core.downloader import mk_update_dir


# This class download help file for using program from the certain ftp server.
class HelpDownloader:
    def __init__(self, server=None):
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
            file = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, file.write)
            file.close()
            ftp.close()
        except Exception as e:
            print('Failed to download from ftp server.', e)
            remove_help(filename)
            raise


def remove_help(filename):
    if os.path.isfile(filename) is True:
        try:
            os.remove(filename)
        except FileNotFoundError as e:
            pass
