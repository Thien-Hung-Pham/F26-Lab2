# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

# Get input from the user for income and marriage status.
income = float(input("Enter your income: "))
status = input("Enter your marriage status (s/m): ").lower()

# Initialize variables to hold the calculated tax amounts.
tax1 = 0
tax2 = 0

# Constant variables for tax brackets based on marriage status.
SINGLE_BRACKET = 32000
MARRIED_BRACKET = 64000
SINGLE_RATE = 0.10
MARRIED_RATE = 0.25

if status == "s":
    if income <= SINGLE_BRACKET:
        tax1 = income * SINGLE_RATE
    else:
        tax1 = (income - SINGLE_BRACKET) * MARRIED_RATE
        tax2 = SINGLE_BRACKET * SINGLE_RATE
else:
    if income <= MARRIED_BRACKET:
        tax1 = income * MARRIED_RATE
    else:
        tax1 = (income - MARRIED_BRACKET) * MARRIED_RATE
        tax2 = MARRIED_BRACKET * MARRIED_RATE

total_tax = tax1 + tax2
income_after_tax = income - total_tax
print(f"Your total tax is: ${total_tax:.2f}")
print(f"Your income before tax is: ${income:.2f}")
print(f"Your income after tax is: ${income_after_tax:.2f}")