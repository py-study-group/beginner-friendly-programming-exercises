# Ask the user for the current value of the BTC, then the percentage of increase/decrease.
bitcoin_value = input("Value of your bitcoin: ")
change_percentage = input("Change% of the BTC: ")

# We need them as numbers, not strings.
bitcoin_value = int(bitcoin_value)
change_percentage = int(change_percentage)

# Calculate by how much the BTC went up or down.
change = (change_percentage / 100) * bitcoin_value

# Print the results.
# The .format is explained in the solution for ex1.
print("New BTC value: {}, it changed with: {}.".format(
    bitcoin_value + change,
    change
))
