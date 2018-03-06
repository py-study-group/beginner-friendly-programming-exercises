# Ask the user for their grades.
geometry = input("Grade for Geometry: ")
algebra = input("Grade for Algebra: ")
physics = input("Grade for Physics: ")

# We need them as numbers, not as strings.
geometry = int(geometry)
algebra = int(algebra)
physics = int(physics)

# Add everything together and divide by 3 to get the average.
average = (geometry + algebra + physics) / 3

# Another possible solution using a list:
# grades = [geometry, algebra, physics]
# average = sum(grades) / len(grades)

print("Your average: " + str(average))

# Encourage the student to work harder.
if average >= 7:
    print("Good job!")
elif 4 < average < 7:
    print("You need to work a little harder.")
else:
    print("You need to work a lot harder.")
