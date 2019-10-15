from psperson import Person


class Employee(Person):
    """derived class """

    def __init__(self, eid, fn, ln):
        self.eid = eid
        super().__init__(fn, ln)  # invoke overridden method

    def get_info(self):
        print('employee id :', self.eid)
        super().get_info()


if __name__ == '__main__':
    e = Employee('v4004', 'guido', 'rossum')
    e.get_info()
