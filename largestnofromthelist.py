# Python program to find largest number in a list
list1 = [10, 20, 30, 40, 32, 8, 51, 22]
# v1 = max(list1)
# print(v1)
# ...................................................
# list1.sort()
# print(list1[-1])
#...........................................
v3 = [x for x in list1]
print(max(v3))

list1.sort(reverse=True)
print(list1[0])
