# Different ways to clear a list in Python

l1 = [2, 3, 4, 3, 2, 1, 4, 5, 6, 3]
# l1.clear()
# print(l1)
# ...........................
# for i in range(len(l1)):
#     l1.pop()
# print(l1)
#.......................................
l1 *= 0
print(l1)
print(".......................................")

v = (map(lambda x: x * 0,l1))
print(list(v))
print(".......................................")

del l1[:]
print(l1)