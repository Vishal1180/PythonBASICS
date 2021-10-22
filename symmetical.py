#ps sting is palindrome
#wow mom
s1 = input(('enter any string'))
#s2 = s1[::-1]
#if s1 == s2:
 #   print('its palindrome')
s2=''.join(reversed(s1))
if s1==s2:
    print('palindrome')


