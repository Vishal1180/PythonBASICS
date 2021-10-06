#Python program to interchange first and last elements in a list
s1 = [1,2,3,4,5]
s1[0],s1[-1]=s1[-1],s1[0]
print(s1)
print('..........................................')


def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list

newList = [12, 35, 9, 56, 24]

print(swapList(newList))