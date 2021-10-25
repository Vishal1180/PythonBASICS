# Inheritance
"""
class Father:
    def m1(self):
        print('m1')
    def __init__(self):
        print('init')
class Child(Father):
    print("IM GUTYLYA")

c = Child()
c.m1()

#multilevel
class Grandfather:
    def __init__(self):
        print("AJOBA")
class Father(Grandfather):
    def __init__(self):
        print("BAAP")
        super().__init__()
class Child(Father):
    def __init__(self):
        print("BETA")
        super().__init__()
c = Child()

# multiple
class Father:
    def __init__(self):
        print("BAAP")
class Mother:
    def __init__(self):
        print("AAAIIIIIEEE")
class Child(Mother,Father):
    def __init__(self):
        print("BETA")
        super().__init__()
c = Child()
print(Child.mro())
"""