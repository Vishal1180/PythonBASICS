#Swap elements in string List
# Swap elements in String list
# using replace() + join() + split()

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + join() + split()
res = ", ".join(test_list)
print(res)
res = res.replace("G", "_").replace("e", "G").replace("_", "e")
print(res)
v = res.split(', ')
print(v)
# printing result
print ("List after performing character swaps : " + str(v))
