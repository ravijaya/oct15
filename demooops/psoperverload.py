class Box:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return Box(self.size + other.size)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Box(self.size * other)
        elif type(other) is Box:   # is, is not identity operator
            return Box(self.size * other.size)

    def __str__(self):
        return f'[{self.__class__.__name__}, size={self.size}]'


if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(11)
    b3 = b1 + b2   # b1.__add__(b2)
    print(b3 * b1)