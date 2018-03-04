# Get the input from the user in the required types.
laptop_price = int(input("Price of laptop: "))
tax = int(input("Tax%: "))

# Add the tax to laptop_price and store it in the laptop_price variable.
laptop_price = (1 + tax / 100) * laptop_price

# Print it.
print("Laptop with tax: " + str(laptop_price))
