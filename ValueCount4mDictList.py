# Write a Python program to count number of items in a dictionary value that is a list.

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2','sss']}
ctr = sum(map(len, dict.values()))
print(ctr)