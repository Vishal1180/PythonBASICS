# Find words which are greater than given length k
# Python program to find all string
# which are greater than given length k

# function find string greater than length k
def string_k(k, str):
    string = []
    text = str.split(" ")
    for x in text:
         if len(x) > k:

            string.append(x)

    return string
k = 3
str = "India is all set to launch GSV-II"
print(string_k(k, str))

