ex6 Solution

# Input the Price of the Laptop
laptopPrice = int(input())

# Input the total Tax
taxPercentage = int(input())

# Calculate the price of the laptop after Tax has been added
totalPrice = int((laptopPrice * taxPercentage / 100) + laptopPrice)

# Print the new Price
print(totalPrice)



ex7 Solution

# Input for Number of Years of Employment
numberOfYears = int(input())

# Input for the total number of Children
totalChildren = int(input())

# Calulate the Total Salary
totalSalary = int(400 + (20 * numberOfYears) + (30 * totalChildren))

print(totalSalary)