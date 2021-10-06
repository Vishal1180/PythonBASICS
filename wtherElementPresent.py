# Python | Ways to check if element exists in list
'''l1 = [1, 2, 3, 4, 5, 6]
element=int(input("Enter any element to check:"))
if element in l1:
    print('Present')
else:
    print('Not present')
#.............................................................
'''
#using Count
l1 = [1, 2, 3, 4, 5, 5, 6]
s = l1.count(10)
#print(s)
if s>0:
    print('present')
else:
    print('Not present')
