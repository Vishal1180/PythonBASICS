# Python | Swap commas and dots in a String
# Difficulty Level : Medium
# Last Updated : 17 Feb, 2021
# The problem is quite simple. Given a string, we need to replace all commas with dots and all dots with the commas. This can be achieved in two popular ways.
# Examples:
#
# Input : 14, 625, 498.002
# Output : 14.625.498, 002

def Replace(str1):
    str1 = str1.replace(', ', 'third')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('third', '.')
    return str1


string = "14, 625, 498.002"
print(Replace(string))

# input: 14, 625, 498.002
#  op: 14.625.498, 002
a = 25, 625, 498.002, 5456.879, 3456.021
a = str(a)
b = a.replace(', ','-').replace('.',', ').replace('-','.')
c =b[1:-1]
print(c)