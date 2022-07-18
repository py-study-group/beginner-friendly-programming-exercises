# Create two variables a and b, and initially set them each to a different number.
# Write a program that swaps both values.

# Example: a = 10, b = 20
# Output: a = 20, b = 10

    
    
def swap_value(a,b):
    A = 0
    B = 0
    A = b
    B = a
    return A, B
    
# test cases
print(swap_value(10, 20))