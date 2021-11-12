# Write a Python program to filter a list of integers using Lambda.
no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(no)
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, no))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, no))
print(odd_nums)