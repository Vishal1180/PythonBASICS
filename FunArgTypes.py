"""
Types of arguments:
    1. positional
    2. keyword
    3. default
    4. variable length

Example:
def display(name,age,salary): #name age sal= parameters/formal arguments
    pass
display('Alok',23,50000)# alok,23,50k= arguments/actual arguments

----------------------------------------------
#1. positional arg: they follow correct sequence or positional order
def display(name,age,salary):
    print('Name:',name,'Age:',age,'Salary:Rs.',salary)

display(26,'Vishal',345436)
# no. of arg. and its position must match otherwise result gets changed
# if we change the order then result gets changed
------------------------------------------------------
#2. keyword arg:
# we can use keywords to pass the values to appropriate locations
#in this position doesnt matter

def display(name,age,salary):
    print('Name:',name,'Age:',age,'Salary:Rs.',salary)

display(age=26,name='Vishal',salary=345436)

# number of actual and formal argument must match
def display(name,age,salary):
    print('Name:',name,'Age:',age,'Salary:Rs.',salary)

display(age=26,name='Vishal',)#in this case u will get a type error
----------------------------------------------------------

# can we use a combination of positional and keyword arguments
def display(name='Mahesh',age,salary):
    print('Name:',name,'Age:',age,'Salary:Rs.',salary)

display(26,2343534)

----------------------------------------------------------
# in above case syntactically its wrong way
# rzn is: non-default argument follows default argument
# we cant use keyword arg. before positional
# if we write a keyword arg after positional then it will work:

def display(age,salary=3565345,name='Amol'):
    print('Name:',name,'Age:',age,'Salary:Rs.',salary)

display(26,name='Ashok')
#----------------------------------------
"""
#3. default arg: in this case we can provide default values for our positional arg
def display(name='Guest'):# name is default
    print('Hello',name)


display('Kedar')
"""
------------------------------------------------

#4. variable length arg:
#when we need to pass variable length input to the function
# then use this option

# in order to declare this: use *
# def add(*n):

def add(*n):
    print(n)

add(10,10)
add(1)
add()
add(1,2,3,4,5,6,7,8,9)
------------------------------------

def add(*n):
    sum=1
    for i in n:
        sum=sum*i
    print(sum)
add(1, 2, 3, 4, 5, 6, 7, 8, 9)
----------------------------------------------
def add(*n,val):
    print(val,n)

add(1,2,3,4,val='A')
----------------------------------------------------------------

#if i want to supply keyword arg. as variable length arg
# for this u need to use: **
# for positional arg: * and for keyword: use **
# it returns a dict
def kw(**v):
    print(v)
#args/kwargs do u know this? what is the use of it?

kw()
kw(name='Akash')
kw(name='Poonam',age=23)
kw(name='Amit',place='Pune',age=45,)
---------------------------------------------------
"""