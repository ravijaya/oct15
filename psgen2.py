def compute(value):
    print(f'received : {value}')

    return bin(value), oct(value), hex(value)


g = (compute(i) for i in range(1, 10))
print(g)
# print()
# print(next(g))

for item in g:
    print(item)
    print('-' * 22)