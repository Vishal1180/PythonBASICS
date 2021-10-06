# Python | Multiply all numbers in the list
input1 = [1, 2, 3]
# prod = 1
# # for i in input1:
# #     prod *= i
# # print(prod)
# s = 0
# while(s<len(input1)):
#     prod *= input1[s]
#     s+=1
# print(prod)
v = input1[0]*input1[1]*input1[2]
print(v)
#..................................................
from functools import reduce as rd
v1 = rd(lambda x,y:x*y,input1)
print(v1)

from math import prod
print(prod(input1))

v2 = [x for x in input1]
print(prod(v2))

import numpy as np
v3 = np.prod(input1)
print(v3)