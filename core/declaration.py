# 서버의 주소나 프로그램 버전과 같은 정보들을 담은 파일입니다.
# 보안의 위험이 있으므로 되도록 배포하지 않는 것이 좋습니다.
import os

CURRENT_VERSION = '0.6'
RELEASED_FILE_DIR = 'Released_files'  # in ftp server.

_current_main_dir = os.getcwd()
TEMP_UPDATE_DIR = os.path.abspath(os.path.join(os.getcwd(), 'tmp_update'))
WORDFINDER_FTP_SERVER = '61.73.209.90'

HELP_FILE = 'help.txt'


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

