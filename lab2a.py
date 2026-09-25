# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
# Purpose: Create a variable, check its type and print the variable.

# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file
x = input("Enter an integer: ")
print(f"Type of x: {type(x)}")

# Convert the input string to an integer.
x = int(x)
print(f"Type of x after conversion: {type(x)}")


# Check whether x is greater than or equal to 6.
if x >= 6:
    print("x is greater then 6!")

# Check whether x is between 4 and 12, inclusive of 4 and exclusive of 12.
if x >= 4 and x < 12:
    print("x is greater than or equal to 4 and less than 12!")