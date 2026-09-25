# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 25/09/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# Import the sys module to access command line arguments.
import sys

num_args = len(sys.argv) - 1

# Check the number of command line arguments provided by the user.
if num_args < 2:
	print("The script requires at least 2 arguments.")
else:
	name = sys.argv[1]
	age = sys.argv[2]
	 
	print(f"Hi {name}, you are {age} years old and the script received {num_args} arguments.")  
