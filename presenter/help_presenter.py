# This class is presenter to present helping script for UI.
# The helping script could be writen in .txt, .md.
class HelpPresenter:
    def __init__(self, filename):
        self.text = ''
        with open(filename, 'r', encoding='utf-8') as file:
            if filename[-4:] == '.txt':
                self.parse_text(file)
            elif filename[-3:] == '.md':
                self.parse_md(file)
            else:
                raise Exception('Cannot parse help file, Wrong extension!')

    def parse_md(self, file):
        for line in file:
            self.text += line

    def parse_text(self, file):
        for line in file:
            self.text += line
