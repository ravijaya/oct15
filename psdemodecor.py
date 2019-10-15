def argument_logger(func):
    def logger_handler(*args):
        value = func(*args)
        print(f'>> {func.__name__} received {args} and returns {value} <<')
        return value

    return logger_handler


def to_json(func):
    def json_handler(*args):
        from json import dumps
        return dumps(func(*args))

    return json_handler


@to_json
@argument_logger
def compute(a, b):
    return dict(result=a + b)


if __name__ == '__main__':
    # compute = argument_logger(compute)
    # compute = argument_logger(to_json(compute))
    print(compute)
    print()
    print(compute(11, 22))
    print()
    print(compute('peter', 'pan'))
