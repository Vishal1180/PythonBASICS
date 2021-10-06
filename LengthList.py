# Python | Ways to find length of list
list1 = [2, 3, 4, 5, 56, 66, 44]
print(len(list1))
print('..............................')

count = 0
for i in list1:
    count += 1
print(count)
print('..............................')
from operator import length_hint
print(length_hint(list1))