# Write a Python program to create a function that
# \takes one argument, and that argument will be multiplied with an unknown given number.

def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
