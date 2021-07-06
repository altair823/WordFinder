# This class is presenter to present helping script for UI.
# The helping script could be writen in .txt, .md.
class HelpPresenter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.text = ''

        if filename[-4:] == '.txt':
            self.parse_text()
        elif filename[-3:] == '.md':
            self.parse_md()
        else:
            raise Exception('Cannot parse help file, Wrong extension!')

    def parse_md(self):
        for line in self.file:
            self.text += line

    def parse_text(self):
        for line in self.file:
            self.text += line
