# File name class for zip and unzip the downloaded updating file.
# For easily converting the extension of files.
class FileName:
    def __init__(self, filename_without_extension):
        self.filename_without_extension = filename_without_extension
        self.zip = filename_without_extension + '.zip'
        self.exe = filename_without_extension + '.exe'
