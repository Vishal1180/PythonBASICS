# Python program to find smallest number in a list
list1 = [10, 20, 9, 30, 40, 50, 8]
print(min(list1))
s = list1[0]
for i in list1:
    if i < s:
        s = i
print(s)
#............................
v2 = [x for x in list1 ]
print(min(v2))
#...........................
v3 = []
v4 = v3.extend(v2)
print(min(v3))
#...........................
list1.sort()
print(list1[0])
#........................
list1.sort(reverse=True)
print(list1[-1])
