from pickle import dump, load


# This class save the current search result.
class FileManager:
    def __init__(self):
        self.mean_dict = {}

    def add_mean(self, dict_type, mean):
        self.mean_dict[dict_type] = mean

    # For caching.
    def save_pickle(self, filename):
        with open(filename, 'wb') as pf:
            dump(self.mean_dict, pf)

    # For saving actual result data.
    def save_text(self, filename):
        with open(filename, 'w') as tf:
            for dict_type, mean in self.mean_dict.items():
                tf.write('\n#'+ dict_type + '#\n')
                tf.write(mean)

    def load_pickle(self, filename):
        pass

    def load_text(self, filename):
        try:
            with open(filename, 'r') as tf:
                dict_type = None
                for line in tf:
                    if line[:1] == '#' and line[-2:] == '#\n':
                        dict_type = line[1:-2]
                        self.mean_dict[dict_type] = ''
                    elif dict_type:
                        self.mean_dict[dict_type] += line
        except Exception:
            raise

        return self.mean_dict
