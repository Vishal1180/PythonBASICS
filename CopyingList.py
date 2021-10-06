# Python | Cloning or Copying a list
#built in copy method
list1 = [22, 33, 44, 55, 66]
l2 = list1.copy()
print(l2)
#using for loop
l3 = []
for i in list1:
    l3.append(i)
print(l3)
#using build in method extend
l4 = []
l4.extend(list1)
print(l4)
#using direct assignment
l5 = list1
print(l5)
#using lambda
l6 = map(lambda x: x, list1)
print(list(l6))
# using list comprehension
l7 =[x for x in list1]
print(l7)
#slicing
l8 = list1[:]
print('l8:',l8)