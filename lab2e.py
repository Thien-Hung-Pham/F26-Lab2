# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 21/09/2026
# Purpose: Check the number of command line arguments.
# Usage: ./lab2e.py <argument1> <argument2>

# Import the sys module to access command line arguments.
import sys


# Check the number of command line arguments provided by the user.
if len(sys.argv) == 1: # 1 means the script name is included in the count, so if len(sys.argv) is 1, it means no additional arguments were provided.
	print("This script requires exactly two arguments. No arguments were provided!")
elif len(sys.argv) != 3: # 3 means the script name and two additional arguments are included in the count, so if len(sys.argv) is not 3, it means the user did not provide exactly two arguments.
	print("This script requires exactly two arguments. You provided " + str(len(sys.argv) - 1) + " arguments.") # str(len(sys.argv) - 1) is used to get the number of arguments provided by the user, excluding the script name.
else:
    print("Hello user, good job, your provided two arguments!")