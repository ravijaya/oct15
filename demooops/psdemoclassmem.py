class MaxConnectionError(Exception):
    """custom exception"""


class Connections:
    """demo for the class members"""
    connection_counter = 0  # class variables
    max_connections = 5

    def __init__(self, connection_id):
        self.connection_id = connection_id
        Connections.connection_counter += 1
        Connections.check_4_limit()

    def __str__(self):
        return f'[{self.__class__.__name__}, connection id={self.connection_id}]'

    @classmethod
    def check_4_limit(cls):
        """class method"""
        if cls.connection_counter > cls.max_connections:
            raise MaxConnectionError('reached the maximum allowed concurrent connections')


def main():
    instances = []

    try:
        for c_id in range(1, 10):
            instances.append(Connections(c_id))

    except MaxConnectionError as err:
        print(err)

    for connection in instances:
        print(connection)


if __name__ == '__main__':
    main()
