from time import sleep

from gui.total_gui import FinderGUI
#from gui.total_gui_test import FinderGUI
from PyQt5.QtWidgets import QApplication
import sys
from core.downloader import rm_update_dir

if __name__ == "__main__" :
    #sleep(1)
    #rm_update_dir()
    app = QApplication(sys.argv)
    word_finder = FinderGUI()
    word_finder.show()
    word_finder.search_word()
    app.exec_()