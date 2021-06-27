import ftplib
from zipfile import ZipFile


ftp = ftplib.FTP('61.73.209.90')
ftp.login()

ftp.cwd('Released_files')
ftp.retrlines('LIST')
ftp.retrbinary('RETR release.zip', open('release.zip', 'wb').write) # README 파일 저장

test_file_name = "release.zip"
with ZipFile(test_file_name, 'r') as zip:
    zip.printdir()
    zip.extractall()
