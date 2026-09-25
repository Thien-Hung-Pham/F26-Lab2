# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
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

SINGLE_THRESHOLD_1 = 8000
SINGLE_THRESHOLD_2 = 32000

MARRIED_THRESHOLD_1 = 16000
MARRIED_THRESHOLD_2 = 64000

if income < 0:
    print("Income cannot be negative. Please enter a valid income.")
    exit()

if status == 's':
    if income <= SINGLE_THRESHOLD_1:
        tax1 = 0.1 * income
    elif income <= SINGLE_THRESHOLD_2:
        tax1 = 0.15 * (income - SINGLE_THRESHOLD_1)
        tax2 = 800
    else:
        tax1 = 0.25 * (income - SINGLE_THRESHOLD_2)
        tax2 = 4400

elif status == 'm':
    if income <= MARRIED_THRESHOLD_1:
        tax1 = 0.1 * income
    elif income <= MARRIED_THRESHOLD_2:
        tax1 = 0.15 * (income - MARRIED_THRESHOLD_1)
        tax2 = 1600
    else:
        tax1 = 0.25 * (income - MARRIED_THRESHOLD_2)
        tax2 = 8800

else:
    print("Invalid marriage status. Please enter 's' for single or 'm' for married.")
    exit()

total_tax = tax1 + tax2
income_after_tax = income - total_tax
print(f"Your total tax is: ${total_tax:.2f}")
print(f"Your income before tax is: ${income:.2f}")
print(f"Your income after tax is: ${income_after_tax:.2f}")