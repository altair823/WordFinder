from core.declaration import WORDFINDER_FTP_SERVER
from core.declaration import CURRENT_VERSION
import ftplib
from core.version_checker import VersionComparator


class UpdateChecker:
    def __init__(self, released_file_dir):
        self.server = WORDFINDER_FTP_SERVER
        self.current_version = ''
        self.target_version = ''
        self.released_file_dir = released_file_dir

    def get_filelist_server(self):
        self.ftp = ftplib.FTP(self.server)
        self.ftp.login()
        self.ftp.cwd(self.released_file_dir)
        return self.ftp.mlsd()

    def get_target_version(self):
        file_list = self.get_filelist_server()
        for i in file_list:
            if 'v#' in i[0]:
                target_version_str = i[0][2:]
                return target_version_str
        # If there is no update file, it means that the supporting is ended.
        # So return version number '0' to update nothing.
        return '0'

    # If the update is needed, return True.
    def check(self):
        if VersionComparator(CURRENT_VERSION, self.get_target_version()).compare() == 1:
            return True
        else:
            return False
