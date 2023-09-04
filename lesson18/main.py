class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle("Tesla", "Model 3")
my_car.get_make_model()



my_car.moves()

your_car = Vehicle("Ford", "Mustang GT")
your_car.get_make_model()
my_car.moves()

######################################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
        