# Python | Sum of all number in List
list1 = [10, 20, 30, 40]
v = sum(list1)
print(v)
#...........................................................
count = 0
for i in list1:
    count = count + i
print(count)
#..................................

v1 = [x for x in list1]
print(sum(v1))
#...............................

count1 = 0
i1 = 0
while i1 < len(list1):
    count1 = count1+list1[i1]
    i1 += 1
print(count1)
# ................................................
from functools import reduce as rd
v3 = rd(lambda x,y: x + y, list1)
print(v3)
