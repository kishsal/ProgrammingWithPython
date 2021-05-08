import sys

def hello(name):
    print('Hello' + name)

name = sys.argv[1]

hello(name)


## Run from cmd prompt 
# pythongh arguments_at_runtime.py joe