# PS:Program to find whether the entered year is leap year or not
year = int(input("Enter the year"))
if year % 4 == 0:
    print("Given year is leap year", year)
else:
    print("Not a leap year")
