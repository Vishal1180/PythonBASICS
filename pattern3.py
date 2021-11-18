'''
12345
2345
345
45
5
45
345
2345
12345

'''
n = 5
for i in range(1, n + 1):
   for j in range(i, n + 1):
        print(j, end="")
   print()
for i in range(1,5):
    for j in range(5-i, 6):
        print(j, end="")
    print()