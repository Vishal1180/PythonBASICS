'''
#13.	Write a program to count the number of digits from any number.
num= float(input("Enter in no"))
count =0
while num != 0:
    num //= 10
    count += 1

print("Number of digits: " , count)
'''
#for i in range(407,500,10)
for i in range(400,500):
    if i%10 == 7:
        print(i)