# Python program to print all even numbers in a range
start = 2
stop1 = 12
for i in range(start,stop1):
    if i % 2 == 0:
        print(i,end=' ')
# taking range values from user
print('\n')
s2 = int(input("Enter the value from where range starts"))
s3 = int(input("Enter the value from where range stops"))

for i in range(s2,s3):
    if i % 2 != 0:
        print(i,end=' ')
