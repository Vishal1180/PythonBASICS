#Maximum of two numbers in Python
a = 2
b = 4

# Use of ternary operator
print(a if a >= b else b)

print(".............................................")
# Python program to find the
# maximum of two numbers


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

# Driver code
a = 2
b = 5
print(maximum(a, b))
print(".............................................")


# Python program to find the minimum of two numbers


def minimum(a, b):
    if a <= b:
        return a
    else:
        return b


# Driver code
a = 2
b = 4
print(minimum(a, b))
