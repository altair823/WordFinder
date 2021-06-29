from itertools import zip_longest


class Version:
    # The version argument must be str formatted with 'x.x.x.x', but unlimited length.
    def __init__(self, version_str='0'):
        self.version = []
        buffer = ''
        for i in version_str:
            if i != '.':
                buffer += i
            else:
                self.version.append(int(buffer))
                buffer = ''
        self.version.append(int(buffer))


class VersionComparator:
    def __init__(self, current_version_str, target_version_str):
        self.current = Version(current_version_str)
        self.target = Version(target_version_str)

    def set_current(self, version_str):
        self.current = Version(version_str)

    def set_target(self, version_str):
        self.target = Version(version_str)

    # Return 1 when the version of target is bigger(newer version),
    # and return -1 when the current version is bigger(this maybe test case version).
    # Return 0 when two versions are same.
    def compare(self):
        for current, target in zip_longest(self.current.version, self.target.version):
            # if current version is newer
            if target is None or (current is not None and current > target):
                return -1
            # if target version is newer
            elif current is None or (target is not None and current < target):
                return 1
        # if two versions are same
        return 0
