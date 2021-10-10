'''l1 = [1,2,3,4,5,1,11,11,3,4,5]
s1 = set(l1)
print(s1)
#anagram means forming new word by rearraging the letter eg BAT and TAB or ABT eg lives elivs
s2 = {'b','a','t','e'}
s3 = {'t','a','e','b',}
if s2 == s3:
    print('anagram')

def m1(a,b):
    add = a + b
    print(add)
m1(10,20)
'''
class Abc:
    def m1(self,v, b):
        add = v + b
        print(add)
ab = Abc()
Abc().m1(12,30)