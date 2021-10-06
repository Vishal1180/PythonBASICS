# Basic list using range() and list Comprehension
digits = [x for x in range(10)]
print(digits)
#Create a List Using Loops and List Comprehension in Python
square = []
for x in range(10):
    square.append(x**2)
print(square)
# using list comprehension
square1 = [x**2 for x in range(10)]
print(square1)
# printing even nos between 1 to 20
even_no = [x for x in range(1,21) if x%2==0 ]
print(even_no)
#Using list comprehensions with strings
# fetching 1st letter of each element in string
list1 = ['Vishal', 'Patil', 'Chikhli','Pune']
v = [x[0] for x in list1]
print(v)

# Using list comprehension for splitting letter in string list
v1 = [x for x in "Vishal is patil"]
print(v1)

# fetching numbers from string using list comprehension
data = "my no is 8275331855"
my_no = [x for x in data if x.isdigit()]
print(my_no)
