# palindrome number
'''
num = int(input("Enter the Number: "))
rev = 0
temp = num
while temp>0:
    rem = temp%10
    rev = rem + (rev*10)
    temp = int(temp/10)
if rev==num:
    print("\nIt is a Palindrome Number")
else:
    print("\nIt is not a Palindrome Number")
'''

s1 = '12321'
s2 = s1[::-1]
s3 = reversed(s1)
print(s3)
if s1 == s2:
    print('its palindrome')
else:
    print('not')