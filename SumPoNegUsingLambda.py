# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list:",nums)

total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))

print("Sum of the positive numbers: ",sum(total_negative_nums))
print("Sum of the negative numbers: ",sum(total_positive_nums))