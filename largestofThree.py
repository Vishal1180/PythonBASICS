"""
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("all are same")

#using function
def maxof3(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
maxof3(10,50,30)
"""
#using List
m1 = [42,20,50]
print(max(m1))
"""from functools import reduce as rd

my_list = [10, 20, 54, 78, 45, 52, 45]
print(rd(lambda r, v: max(r, v), my_list))
"""
