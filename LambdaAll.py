input1 = [1, 2, 3]
from functools import reduce as rd  # gives single value output based on all input values

v1 = rd(lambda x, y: x * y, input1)
print(v1)
v2 = map(lambda x: x + 2, input1)  # return List by performing iteration on each element based on given condition
print(list(v2))
v3 = filter(lambda x: x > 1, input1)  # return only true values for which the condition matches
print(list(v3))
