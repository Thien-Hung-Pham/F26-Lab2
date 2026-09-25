# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO 1: 
# Import the `math` module.
import math
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.
num = float(input("Please enter a number: "))

# TO DO 2: 
# Create an infinite loop using while True. Inside the loop:
while True:
# Check if num is negative:
    if num < 0:
        # If it is, print "Invalid number." and continue to the next iteration of the loop.
        print("Invalid number.")
        num = float(input("Please enter a number: "))
        continue

# TO DO 3: 
# Check if num is zero:
    if num == 0:
        # If it is, print "Exiting..." and break out of the loop.
        print("Exiting...")
        break


# TO DO 4: 
#Calculate the square root of num using the math.sqrt function.
    if num > 0:
        sqrt_num = math.sqrt(num)
        print(f"The square root of {num} is {sqrt_num}.")
        num = float(input("Please enter a number: "))
 