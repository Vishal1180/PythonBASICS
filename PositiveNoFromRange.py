# Python program to print all positive numbers in a range
start, end = -9, 11
for num in range(start, end + 1):
    if num >= 0:
        print(num, end=" ")
