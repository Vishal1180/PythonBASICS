'''
#Program to print half pyramid using *
*
* *
* * *
* * * *
* * * * *

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
'''

for i in range(6):
    print(i*' *')