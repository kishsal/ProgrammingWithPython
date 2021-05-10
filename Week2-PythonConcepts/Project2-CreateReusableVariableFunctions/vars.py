# Name here is a local variable
def hello():
    name = "Mike"
    print('Hello' + name)

hello()


# Name here is a global variable
name = "Mike"

def hello():    
    print('Hello' + name)

def goodbye():    
    print('Goodbye' + name)

hello()
goodbye()

