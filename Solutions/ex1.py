# Set the values
a = 10
b = 20

# Set a to b, and b to a
a, b = b, a

# The .format replaces all {} respectively with values in the .format
print("a = {}, b = {}".format(
    a,  # Replace the first {} with the (new) value of a.
    b   # Replace the second {} with the (new) value of b.
))
