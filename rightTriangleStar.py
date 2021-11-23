"""
Right triangle star Pattern
    *
   **
  ***
 ****
*****
"""
# right triangle star pattern
size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()
"""
# Left triangle star pattern
size = 5
for i in range(1, size+1):
    print(" " * (size - i) + "*" * i)
"""