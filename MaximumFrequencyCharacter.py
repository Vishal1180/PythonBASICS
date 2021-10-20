# Python 3 code to demonstrate
# Maximum frequency character in String
# collections.Counter() + max()
from collections import Counter

# initializing string
test_str = "Nitin"

# printing original string
print ("The original string is : " + test_str)

# using collections.Counter() + max() to get
# Maximum frequency character in String
res = Counter(test_str)
res = max(res, key = res.get)

# printing result
print ("The maximum of all characters in Nitin is : " + str(res))
