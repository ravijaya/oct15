"""access specifier"""


class PackageManager:
    def __init__(self, name, version):
        self.__name = name   # private attribute
        self.version = version

    def __get_information(self):
        """private method"""
        print('name :', self.__name)
        print('version :', self.version)

    def wrapper(self):
        """public method"""
        self.__get_information()


if __name__ == '__main__':
    pm = PackageManager('pip', '2.2.18')
    pm.wrapper()
    # print(pm.__name)
