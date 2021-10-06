# Python | Count occurrences of an element in a list
list1 = [22, 33, 44, 55, 66, 66, 33, 44, 55, 55]

#l2 = int(input("Enter element to count:"))
# l3 = list1.count(l2)
# print(l3)
# count = 0
# for i in list1:
#     if i == l2:
#         count+=1
# print(count)
#
#
# from collections import Counter
# l4 = Counter(list1)
# print(l4[l2])

# To get exact numbers of occurrences using Dictionary
from collections import Counter
l4 = dict(Counter(list1))
print(l4)

