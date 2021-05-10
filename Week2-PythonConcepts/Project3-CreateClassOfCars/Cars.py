# Creating a class, init function assigns values to object properties 

class Cars:
    def __init__(self, model, make, year):
        self.model = "Ford"
        self.make = make
        self.year = year

    def print_model(self):
        print(self.model)

    def print_make_and_year(self, make, year):
        print(make)
        print(self.year)

# my_cars variable
my_cars =  Cars("Ford","F150","2020")


print(my_cars.print_model())