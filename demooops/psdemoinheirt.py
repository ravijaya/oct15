class Alpha:
    def pprint(self):
        print('pprint from class Alpha')


class Beta(Alpha):
    def pprint(self):
        print('pprint from the class Beta')
        super().pprint()


class Charlie(Beta):
    def pprint(self):
        print('pprint from the class Charlie')
        super(Beta, self).pprint()


if __name__ == '__main__':
    Charlie().pprint()