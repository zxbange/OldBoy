import os
import pickle


class Mypickle(object):

    def __init__(self, path_name):
        self.path_name = path_name

    def dump(self, obj):
        with open(self.path_name, "ab") as f:
            pickle.dump(obj, f)

    def load(self):
        if os.path.isfile(self.path_name):
            with open(self.path_name, "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                        yield data
                    except Exception as e:
                        break

    def edit(self, obj):
        pass