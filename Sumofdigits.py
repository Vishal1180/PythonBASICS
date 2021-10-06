# Python | Sum of number digits in List
# input = [11,22,33]
# output=[2,4,6]
input = [11, 22, 33]
v = []
for i in input: # to get 11 22 33
    s = 0
    for j in str(i):
        s += int(j)
    v.append(s)
print(v)

#..................................
# s1 = 123454534
# s2 = str(s1)
# for i in s2:
#     print(i,end=' ')
from functools import reduce
res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in input]
print(res)