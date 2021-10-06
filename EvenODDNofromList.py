# Python program to print even numbers in a list
a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     if i % 2 == 0:
#         print(i)
# using while loop
# i = 1
# while (i <= len(a)):
#     if i % 2 == 0:
#         print(i,end=' ')
#     i += 1
# using List comprehension
v1 = [x for x in a if x % 2 == 0]
print(v1)

#using lambda function
v2 = filter(lambda x:x % 2 ==0,a)
print(list(v2))

#ODD numbers
for i in a:
    if i % 2 != 0:
        print(i)
# using while loop
# i = 1
# while (i <= len(a)):
#     if i % 2 != 0:
#         print(i,end=' ')
#     i += 1
# using List comprehension
v3 = [x for x in a if x % 2 != 0]
print(v3)

#using lambda function
v4 = filter(lambda x:x % 2 !=0,a)
print(list(v4))

