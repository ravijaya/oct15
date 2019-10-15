items = [2, 1, 3]

temp = [item ** 2 for item in items]   # list comprehension
print(temp)
print()

temp = (item ** 2 for item in items)   # generator expression
# print(temp)
# print(next(temp))
# print(next(temp))
# print(next(temp))
# print(next(temp))

temp2 = (bin(i) for i in items)
for item in temp2:
    print(item)
