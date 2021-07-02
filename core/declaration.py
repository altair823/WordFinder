# This file violate the Dependency Inversion Principle,
# because other modules depend on this module.


# Temporary directory that will contains downloaded files which is replaced the original files.
# And the old files will moving this temp_dir.
import os

CURRENT_VERSION = '0.4.4'
RELEASED_FILE_DIR = 'Released_files'  # in ftp server.

_current_main_dir = os.getcwd()
TEMP_UPDATE_DIR = os.path.abspath(os.path.join(os.getcwd(), 'tmp_update'))
WORDFINDER_FTP_SERVER = '61.73.209.90'


# In the test environment, there should exist '.TEST' file.
def is_this_test():
    # In user environment,
    if __name__ != '__main__':
        for i in os.listdir(os.getcwd()):
            if '.TEST' in i:
                return True
        return False
    # In test environment,
    else:
        for i in os.listdir(os.pardir):
            if '.TEST' in i:
                return True
        return False

IS_THIS_TEST = is_this_test()

