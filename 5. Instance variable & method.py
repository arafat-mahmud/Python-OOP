class Car:
    def __init__(self, name, model):
        self.name = name
        self.model_year = model
        self.wheel = 4

    def view(self):
        print("The  model year of this", self.name, "is", self.model_year)
        print("It is a", self.wheel, "wheel car.")

c1 = Car("BMW", 2010)
c2 = Car("Tesla Model S", 2015)

c1.view()
c2.view()
