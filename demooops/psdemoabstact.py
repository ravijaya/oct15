"""abstact class and method"""

from zipfile import ZipFile
from tarfile import TarFile
from glob import glob
from abc import ABC, abstractmethod

"""http://collabedit.com/k32ht"""


class UnSupportedArchiveError(Exception):
    """user defined exception"""


class ArchiveManager(ABC):
    """abstract class"""

    @abstractmethod
    def save(self):
        """abstract method"""


class ZipArchive(ArchiveManager):
    """concrete class"""

    def __init__(self, name):
        self.name = name

    def save(self, *args):
        with ZipFile(self.name, mode='w') as zf:
            for file_name in args:
                zf.write(file_name)
                print(f'{file_name}: added')


class TarArchive(ArchiveManager):
    pass


def make_archive(archive_name, archive_type='zip'):
    """factory method"""

    if archive_type == 'zip':
        archive = ZipArchive(archive_name)
    elif archive_type == 'tar':
        archive = TarArchive(archive_name)
    else:
        raise UnSupportedArchiveError(f'not yet supported : {archive_type}')

    return archive


if __name__ == '__main__':
    archive = make_archive('src.zip')
    archive.save(*glob('*.py'))
