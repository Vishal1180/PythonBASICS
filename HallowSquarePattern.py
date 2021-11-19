"""Hollow Square Pattern
*****
*   *
*   *
*   *
*****
"""
# hollow square pattern
size = 5
for i in range(size):
    for j in range(size):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()