'''11.	Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
a.	For first 50 units Rs. 0.50/unit
b.	For next 100 units Rs. 0.75/unit
c.	For next 100 units Rs. 1.20/unit
d.	For unit above 250 Rs. 1.50/unit
e.	An additional surcharge of 20% is added to the bill
'''
unit=int(input("enter the no of units"))
if unit <= 50:
    bill =.50*unit
elif unit <=150:
    bill =.75*unit
elif unit <=250:
    bill =1.2*unit
else:
    bill = 1.5*unit

final_bill=bill+(bill*.2)
print('Final bill:',final_bill)