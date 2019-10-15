def get_integers():
    """infinite stream"""
    i = 1

    while True:
        yield i
        i += 1


square = (item ** 2 for item in get_integers())


def take_n(seq, count):
    return (next(seq) for _ in range(count))


for element in take_n(square, 5):
    print(element)
