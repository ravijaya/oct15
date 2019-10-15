"""demo for the functional programming"""

items = [11, 13, 12, 12, 14, 13, 15, 14, 19, 16, 17, 18]

m = map(hex, items)
m2 = map(str.upper, m)


for item in m2:
    print(item)


m = map(ord, 'peter pan')
print(list(m))