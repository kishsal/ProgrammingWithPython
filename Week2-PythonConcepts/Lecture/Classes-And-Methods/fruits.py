class Fruits: # Always capital
    # Use the __init__() function to assign values to object properties
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color


# Initiate the class
fruit = Fruits('Banana', 'Yellow')

print(fruit.color)

print(fruit.fruit)