# Python program to sort a list of
# tuples by the second Item using sort()

# Function to sort hte list by second item of tuple
def Sort_Tuple(tup):
	tup.sort(key = lambda x: x[1])
	return tup

# Driver Code
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

print(Sort_Tuple(tup))

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python program to sort a list of
# tuples by the second Item using sorted()

# Function to sort the list by second item of tuple
def Sort_Tuple(tup):
	return(sorted(tup, key = lambda x: x[1]))

# Driver Code
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

# printing the sorted list of tuples
print(Sort_Tuple(tup))
