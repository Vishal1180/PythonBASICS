# Write a Python program to find palindromes in a given list of strings using Lambda.
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
print("\nList of palindromes:")
print(result)