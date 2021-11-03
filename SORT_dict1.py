#Sort Python Dictionaries by Key or Value
# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
