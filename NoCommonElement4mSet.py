# Write a Python program to check if two given sets have no elements in common.
x = {1,2,3,4}
y = {4,5,6,7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)
print("\nConfirm two given sets have no element(s) in common:")
print("\nCompare x and y:")
print(x.isdisjoint(y))
print("\nCompare x and z:")
print(z.isdisjoint(x))
print("\nCompare y and z:")
print(y.isdisjoint(z))