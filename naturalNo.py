'''
#print 1 to N natural no using while loop
n = int(input('Enter the value of n:'))
i = 1
while i<=n:
    print(i)
    i+=1


#reverse natural numbers
n = int(input('Enter the value of n:'))
while n>=1:
    print(n)
    n-=1

#wap to print all alphabets from a to z using while loop

s = 97
while s <= 122:
    print(chr(s), end=" ")
    s += 1
'''
# multipication table
n=int (input('Enter the number:'))
for i in range(1,11):
    print(i*n)