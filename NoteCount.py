nominals = (2000, 500, 100, 50, 20, 5, 1)
amount = int(input('amount = '))
output = {}
count=0
for n in nominals:
	output[n] = amount // n
	amount %= n
for k, v in output.items():
	print(k, v, sep=':')
	count+=v
print('Total numbers of currency notes ',count)

'''
def countCurrency(amount):
	notes = [2000, 500, 200, 100,
			 50, 20, 10, 5, 1]

	noteCounter = [0, 0, 0, 0, 0,
				   0, 0, 0, 0]

	print("Currency Count -> ")

	for i, j in zip(notes, noteCounter):
		if amount >= i:
			j = amount // i
			amount = amount - j * i
			print(i, " : ", j)


# Driver code
amount = 868
countCurrency(amount)

#code 3

Amount = input("Please Enter Amount for Withdraw :")

print "\n\nRequired notes of 100 is : " , Amount / 100
print "Required notes of 50 is : " , (Amount % 100) / 50
print "Required notes of 10 is : " , (((Amount % 100) % 50) / 10)
print "Amount still remaining is : " , (((Amount % 100) % 50) % 10)


'''