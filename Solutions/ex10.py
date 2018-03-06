# Get the input from the user
number = int(input("A number: "))

# To get the last number, we divide by ten, round the number down, multiply it by 10 and subtract it from the number variable.
# The division and rounding down happens in one step using the // operator.
to_subtract = 10 * (number // 10)

# Now we subtract them to get the last digit
last_digit = number - to_subtract

# Print it out
# .format() is explained in previous solutions.
print("The last digit of {} is: {}".format(number, last_digit))


# The easiest way to do it is using substrings, which is where you grab a specific part of a string.
# Sadly this wasn't allowed in this exercise.
# If it were, you'd have this as solution:

# number = input("A number: ")  # Notice the int() is gone. We do this to get a string, not an integer.
# last_digit = number[-1] # We need the last character of number. -1 is a short operator for that, -2 for the second to last character, etc.
#
# print("The last digit of {} is: {}".format(number, last_digit))
