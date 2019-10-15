def compute(a, b, c):
    return a + b + c


def sqr(n):
    return n ** 2


# parallel iterate
items1 = [1, 2, 3]
items2 = [1, 2, 3]
items3 = [3, 2, 1]

m = map(compute, items1, items2, items3)

m = map(sqr, items1)
for item in m:
    print(item)

print()

for item in zip(['pam', 'sam', 'jim'], ['female', 'male', 'male'], [3, 4]):  # parallel iteration
    print('{:<22}  {:<9}  {}'.format(*item) )

