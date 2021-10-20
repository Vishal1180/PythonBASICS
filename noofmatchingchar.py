# Count the Number of matching characters in a pair of string
str1 = 'vishal'
str2 = 'patil'
count = 0
for i in str1:
    if i in str2:
        count +=1
print(count)