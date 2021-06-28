from core.declaration import WORDFINDER_FTP_SERVER
from core.declaration import VERSION
from core.declaration import RELEASED_FILE_DIR
import ftplib


class UpdateChecker:
    def __init__(self, released_file_dir):
        self.server = WORDFINDER_FTP_SERVER
        self.version = VERSION
        self.released_file_dir = released_file_dir

    def get_filelist_server(self):
        self.ftp = ftplib.FTP(self.server)
        self.ftp.login()
        self.ftp.cwd(self.released_file_dir)
        return self.ftp.mlsd()

    def check(self):
        file_list = self.get_filelist_server()
        for i in file_list:
            if 'v#' in i[0]:
                print(i[0][2:])

UpdateChecker(RELEASED_FILE_DIR).check()