class VersionChecker:
    def __init__(self):
        self.current = ''
        self.target = ''

    def set_current(self, version):
        if version