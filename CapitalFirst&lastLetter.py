# Python program to capitalize the first and last character of each word in a string
s1 = 'vishal patil'
# s2 = []
# for i in s1.split():
#     s = i[0].upper()
#     s3 = i[-1].upper()
#     s4 = s + i[1:-1] + s3
#     s2.append(s4)
# print(' '.join(s2))
# s5 = ' '.join(s2)
# print(type(s5))
s2 = s1.split()
for i in range(len(s2)):
    s3 = s2[i][0].capitalize() + s2[i][1:-1] + s2[i][-1].capitalize()
    #s4 = s2[i][0].capitalize() + s2[i][1:-1] + s2[i][-1].capitalize()
    print(s3,end=' ')



