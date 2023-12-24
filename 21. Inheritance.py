class Animal:

    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is braking")

# Create instances
a1 = Animal("Jack")
d1 = Dog("Rover")

# Call methods
d1.bark()
d1.eat()

a1.eat()

