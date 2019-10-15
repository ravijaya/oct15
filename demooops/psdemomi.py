class Alpha:
    def pprint(self):
        print('pprint from class Alpha')


class Beta:
    def pprint(self):
        print('pprint from the class Beta')


class Charlie(Beta, Alpha):
    def pprint(self):
        super().pprint()
        # Alpha.pprint(self)
        # Beta.pprint(self)


if __name__ == '__main__':
    Charlie().pprint()
    print(Charlie.mro())  # method resolution order
