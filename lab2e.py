# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
# Purpose: Check the number of command line arguments.
# Usage: ./lab2e.py <argument1> <argument2>

# Import the sys module to access command line arguments.
import sys

nums_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name from the count.

# Check the number of command line arguments provided by the user.
if nums_args == 1:  
	print("This script requires exactly two arguments. No arguments were provided!")

elif nums_args != 2:
	# str(nums_args) is used to convert the number of arguments provided by the user to string.
	print("This script requires exactly two arguments. You provided " + str(nums_args) + " arguments.") 
	
else:
    print("Hello user, good job, your provided two arguments!")