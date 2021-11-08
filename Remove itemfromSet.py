# Python program to remove elements from set
# Using the pop() method
def Remove(initial_set):
	while initial_set:
		initial_set.pop()
		print(initial_set)

# Driver Code
initial_set = set([12, 10, 13, 15, 8, 9])
Remove(initial_set)
