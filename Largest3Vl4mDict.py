# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

from heapq import nlargest
my_dict = {'a':500, 'b':574, 'c': 560,'d':400, 'e':5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 