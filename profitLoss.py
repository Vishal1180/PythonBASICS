#program to calculate profit or loss
Actual_cost = float(input("Enter a Actual Cost in rupees:"))
Selling_cost = float(input("Enter a Selling cost in rupees:"))
if Selling_cost > Actual_cost:
    print('Its Profit of Rs',Selling_cost-Actual_cost)
else:
    print('Its Loss of Rs',Selling_cost-Actual_cost)
