'''10.	Write a program to input basic salary of an employee and calculate its gross salary according to following:
a.	Basic Salary <= 10000 : HRA = 20%, DA = 80%
b.	Basic Salary <= 20000 : HRA = 25%, DA = 90%
c.	Basic Salary > 20000 : HRA = 30%, DA = 95%
'''
salary=float(input('Enter the salary'))
if salary<=10000:
    HRA=0.2*salary
    DA= 0.8 * salary
    gross_salary=salary+HRA+DA
elif salary<=20000:
    HRA=0.25*salary
    DA= 0.9 * salary
    gross_salary=salary+HRA+DA
else:
    HRA = 0.3 * salary
    DA = 0.95 * salary
    gross_salary = salary + HRA + DA
print("Gross salary is:",gross_salary)