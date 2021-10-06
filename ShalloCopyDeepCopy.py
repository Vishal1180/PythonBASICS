# Concept of shallow Copy and Deep Copy
list1 = [11,22,33,44]
list2 = list1.copy() #shallow copy
print(list1)
print(list2)
print(id(list1)) #Different id
print(id(list2))
list1[1]=55  #only in list 1
print(list1)
print(list2)
list3 = list1  # deep copy
print(list1)
print(list3)
print(id(list1))# id same
print(id(list3))
list1[2]=88
print(list1)
print(list3)