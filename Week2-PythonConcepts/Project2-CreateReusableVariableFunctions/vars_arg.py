# This allow you to provide an argument.

import sys

def hello(name):    
    print('Hello ' + name)

name = sys.argv[1]

hello(name)

# To run this, enter python ./vars_arg.py Tom