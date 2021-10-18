# Program to check whether input angles of triangle and check its a triangle or not
angle1 = int(input('Enter size of angle1'))
angle2 = int(input('Enter size of angle2'))
angle3 = int(input('Enter size of angle3'))
sum = angle3+angle2+angle1
if sum==180:
    print('Its a triangle')
else:
    print('Not a valid triangle')