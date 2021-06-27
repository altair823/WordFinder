import ftplib
from zipfile import ZipFile


class Updater:
    def __init__(self):
        self.server = '61.73.209.90'
        self.filename = 'WordFinder'

    def update(self):
        ftp = ftplib.FTP(self.server)
        ftp.login()
        ftp.cwd('Released_files')
        ftp.retrbinary('RETR ' + self.filename + '.zip', open(self.filename + '.zip', 'wb').write)
        with ZipFile(self.filename + '.zip', 'r') as zip:
            zip.extractall()
