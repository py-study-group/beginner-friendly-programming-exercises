# Get the input from the user in the required types.
years_worked = int(input("How many years have you worked: "))
children = int(input("How many children do you have: "))
miss_a_day = input("Did you miss a day of work (y/n): ")

# Validate and parse miss_a_day
# For easy comparison, we make everything entered lowercase.
if miss_a_day.lower() == "y" or miss_a_day.lower() == "yes":
    miss_a_day = 0
else:
    miss_a_day = 100

# Salary is:
# 400 minimum wage,
# 20 for every year worked,
# 30 for each child the employee has,
# 100 if the employee didn't miss a day of work.
salary = 400 + 20 * years_worked + 30 * children + miss_a_day

# Print it.
# Notice the \t character. That stands for a TAB. It makes everything align pretty nicely.
print("Your salary:")
print("Minimum wage:\t\t\t\t400")
print("Years of experience:\t\t" + str(20 * years_worked))
print("Support for your children:\t" + str(30 * children))
print("All-days-worked bonus:\t\t" + str(miss_a_day))
print()  # This is for an empty newline
print("Total:\t\t\t\t\t\t" + str(salary))
