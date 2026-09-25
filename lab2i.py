# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

# Follow the specific instructions given in the README.md file.
# TO DO 1: 
# Creat variable pin. The value of pin should be a 4 digit code inputted by the user.
pin = input("Please type in your PIN: ")

# Add a while loop to create program that wont end until the user enters 1234.
correct_pin = "1234"
while pin != correct_pin:
    print("Incorrect PIN, try again...\n")
    pin = input("Please type in your PIN: ")
print("Correct PIN, You can enter!")
