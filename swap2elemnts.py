# Python program to swap two elements in a list
s = [22, 33, 44, 55, 66]

temp = s[2]
s[2] = s[1]
s[1] = temp
print(s)
print('........................................')


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))

print('................................................')

f1 = [22, 33, 55, 7788, 66, 11]

a = f1.pop(3)
b = f1.pop(-1)
f1.append(a)
f1.insert(3,b)
print(f1)