# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 21/09/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# Import the sys module to access command line arguments.
import sys


# Check the number of command line arguments provided by the user.
if len(sys.argv) < 3:
	print("The script requires at least 2 arguments.")
elif len(sys.argv) >= 3:
	name = sys.argv[1]
	age = sys.argv[2]
	arguments = len(sys.argv) - 1
	print(f"Hi {name}, you are {age} years old and the script received {arguments} arguments.")
