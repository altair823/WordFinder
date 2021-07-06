from PyQt5.QtWidgets import QDialog, QMessageBox

from core.declaration import WORDFINDER_FTP_SERVER, HELP_FILE
from core.help_downloader import HelpDownloader, remove_help
from resource.help_window import Ui_help_window
from presenter.help_presenter import HelpPresenter


# GUI for help text window.
class HelpWindow(QDialog, Ui_help_window):
    def __init__(self, parent):
        super(HelpWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('도움말')

        try:
            # Download help file.
            HelpDownloader(server=WORDFINDER_FTP_SERVER).download(HELP_FILE)
        except Exception:
            QMessageBox.critical(self, '오류', '도움말 파일을 열 수 없습니다!')
            return

        self.help_text_label.setText(HelpPresenter(HELP_FILE).text)
        remove_help(HELP_FILE)
        self.show()
        self.exec_()