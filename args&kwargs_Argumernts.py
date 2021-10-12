'''
def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:", sum)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

'''
import random
print(random.randrange(1,19))
print(random.randint(1,6))