items = list(range(1, 200))

print(items)
print()

m = filter(lambda n: n % 7 == 0, items)
print(m)
print(type(m))
print(list(m))
