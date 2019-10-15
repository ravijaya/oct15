from psdirlisting import DirectoryListing
from json import dump


class DirectoryListing2JSON(DirectoryListing):
    """demo for the inheritance"""
    def to_json(self, json_file):
        try:
            dump(self.container, open(json_file, 'w'), indent=2)
        except IOError as err:
            print(err)


if __name__ == '__main__':
    DirectoryListing2JSON('/tmp', '/home/ravijaya', '/home/ravijaya/Downloads').to_json('tmp.json')