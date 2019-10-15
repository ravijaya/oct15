from os import listdir
from os.path import isfile, join, getsize, getmtime, basename
from time import ctime
from pprint import pprint as pp
from psdemodecor import argument_logger


class DirectoryListing:
    container = dict()

    @argument_logger
    def __init__(self, *args):
        self.directories = args
        self.read_directories()

    def read_directories(self):
        for dir_name in self.directories:
            m = map(lambda item: join(dir_name, item), listdir(dir_name))

            for file_name in filter(isfile, m):
                file_properties = [getsize(file_name), ctime(getmtime(file_name))]
                file_name = basename(file_name)
                self.container.setdefault(dir_name, {})[file_name] = file_properties


if __name__ == '__main__':
    dl = DirectoryListing('/tmp', '/home/ravijaya', '/home/ravijaya/Downloads')
    pp(dl.container)

"""
{
   'd1': {'f1': [size, mtime], f2: [size, ts]}, ....
}
"""
