# Python: Get a string from a given string where all occurrences of
# its first char have been changed to '$',
# except the first char itself
s1 = 'nitin'
s2 = s1[0]
s3 = s1[1:].replace(s2,'$')
s4 = s2 + s3
print(s4)