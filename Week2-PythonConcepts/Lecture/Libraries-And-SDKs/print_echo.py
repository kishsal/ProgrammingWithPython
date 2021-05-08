# Use the OS and Sys library
import os
import sys

# Define a function that used the 'os' library
def echo_name(name):
    # Use the 'system()' method from the 'os' library
    print_name = os.system("Echo hello, " + name)
    print(print_name)

# use the 'sys' library to pass in a value at runtime
name = sys.argv[1]

echo_name(name)