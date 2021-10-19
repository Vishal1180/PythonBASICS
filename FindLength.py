#ps: Find length of string
'''
s1 = 'Welcome to Python'
#print(len(s1))

count = 0
for i in s1:
    count +=1
print(count)

from operator import length_hint
print(length_hint(s1))

def len(s):
    count = 0
    for i in s:
        count += 1
    return count
print(len(s1))
# Python code to demonstrate string length
# using while loop.

# Returns length of string
def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = "geeks"
print(findLen(str))
'''

# Python code to demonstrate string length
# using join and count

# Returns length of string
def findLen(str):
	if not str:
		return 0
	else:
		some_random_str = 'py'
		return ((some_random_str).join(str)).count(some_random_str) + 1

str = "geeks"
print(findLen(str))

