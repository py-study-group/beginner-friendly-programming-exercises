# Get the input from the user in the required types.
years_worked = int(input("How many years have you worked: "))
children = int(input("How many children do you have: "))

# Salary is:
# 400 minimum wage,
# 20 for every year worked,
# 30 for each child the employee has.
salary = 400 + 20 * years_worked + 30 * children

# Print it.
# Notice the \t character. That stands for a TAB. It makes everything align pretty nicely.
print("Your salary:")
print("Minimum wage:\t\t\t\t400")
print("Years of experience:\t\t" + str(20 * years_worked))
print("Support for your children:\t" + str(30 * children))
print()  # This is for an empty newline
print("Total:\t\t\t\t\t\t" + str(salary))
