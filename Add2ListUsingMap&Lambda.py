# Write a Python program to add two given lists using map and lambda.

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = map(lambda x, y: x + y, nums1, nums2)
print("\nResult: after adding two list")
print(list(result))