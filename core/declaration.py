

# Temporary directory that will contains downloaded files which is replaced the original files.
# And the old files will moving this temp_dir.
import os

VERSION = '0.3'
RELEASED_FILE_DIR = 'Released_files'

temp_update_dir = os.path.abspath(os.path.join(os.getcwd(), 'tmp_update'))
WORDFINDER_FTP_SERVER = '61.73.209.90'
