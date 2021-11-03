#Write a program to find diameter, circumference and area of circle.
#use of math module
from math import pi
radius = float(input("Enter the value of radius:"))
Diameter = 2 * radius
Cir = 2 * pi
Area = pi * Diameter

print("Diameter of circle is:",Diameter)
print("Circumference of circle is:",Cir)
print("Area of circle is:",Area)
