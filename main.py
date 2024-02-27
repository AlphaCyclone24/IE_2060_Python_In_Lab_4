# Library imports
import numpy

# Setting variables
total = 0
i = 0
a = 1
# Getting user input
n = int(input(f"What is your number?"))

# If the number is less than zero, have the problem end.
if n < 0:
    print(f"The number is less than zero please enter a different number")

# If the number is greater than zero have the program continue
elif n > 0:
    # Acts like a summation, adds everything together until it gets to the end number
    while i != n:
        # Math for the equation
        k = numpy.log(a * 100) ** 2
        # Keeping a running total for the summation
        total = total + k
        # Tells the program how many times it has run
        i = i + 1
        # Tells the program what number it is on
        a = a + 1
        # Tells the user which one it has computed
        print(f"{i}")
        # Tells the user the overall total
        print(f"The answer is: {total}")
