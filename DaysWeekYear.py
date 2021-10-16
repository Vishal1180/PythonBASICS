#6.	Write a program to convert days into years, weeks and days.
'''
num = int(input('Enter the Number of Days:'))
year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)
print("Total Number of Year(s): ",year)
print("Total Number of Week(s):",week)
print("Total Number of Day(s):",days)
'''
# using function
# Python3 code to convert given number of days in terms of  Years, Weeks and Days

DAYS_IN_WEEK = 7


# Function to find
# year, week, days
def find(number_of_days):
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
               DAYS_IN_WEEK)
    days = (number_of_days % 365) % DAYS_IN_WEEK
    print("years = ", year,
          "\nweeks = ", week,
          "\ndays = ", days)

number_of_days = 200
find(number_of_days)

