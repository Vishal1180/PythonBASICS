# Python program to count Even and Odd numbers in a List
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 50, 22, 44, 77, 40, 28, 56]
# even_count = 0
# odd_count = 0
# for i in l1:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(even_count)
# print(odd_count)
# using lambda function
even_no = list(filter(lambda x:x%2 == 0,l1))
print(even_no)
print(len(even_no))
odd_no = list(filter(lambda x:x%2 != 0,l1))
print(odd_no)
print(len(odd_no))