# WAP to calculate factorial of number using function

"""
def factorial(num):
    result = 1
    for i in range(num):
        result = result * num
        num -= 1
    return result
print(factorial(5))
"""


# WAP to find a factorial for 1-10 numbers using function

def function(num):
    result = 1
    for i in range(num):
        result = result * num  # 12*2=12
        num -= 1
    return result


for i in range(1, 11):
    print('factorial of', i, 'is', function(i))
# o = function(10)
# factorial of 1 is 1
# factorial of 2 is 2
# factorial of 3 is 6
# print(o)
# --------------------------
