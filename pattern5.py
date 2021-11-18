'''22.	Write a program to print following Pattern:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def contnum(n):
    # initializing starting number
    num = 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # not re assigning num
        # num = 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(num, end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")


n = 5

# sending 5 as argument
# calling Function
contnum(n)
