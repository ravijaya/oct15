def demo():
    """generator function"""

    print('before 1')
    yield 123
    print('after 1')

    print('before 2')
    yield 12.21
    print('after 2')

    print('before 3')
    yield 'pam'
    print('after 3')


for item in demo():
    print(item)
    print('-' * 22)
    
# g = demo()
# print(next(g))
# print('-' * 22)
#
# print(next(g))
# print('-' * 22)
#
# print(next(g))
# print('-' * 22)
#
# print(next(g))
# print('-' * 22)
