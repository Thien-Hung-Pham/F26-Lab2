# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
for fruit in fruits:
   print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.
for i in range(5):
   print(i)

# Initialize a variable to hold the sum of even numbers
sum = 0

for num in range(1, 101): # Run from 1 to 100
   if num % 2 == 0: # Check if the number is even
      sum += num
print(f"Final sum: {sum}")