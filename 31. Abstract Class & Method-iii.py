from abc import ABC,abstractmethod
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def eat(self):
        print("He is eating")

class Dog(Animal):
    def make_sound(self):
        print("Dog barking")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")

class Snake(Animal):
    def make_sound(self):
        print("Hiss Hiss")

d1 = Dog()
d1.eat()
d1.make_sound()

c1 = Cat()
c1.eat()
c1.make_sound()

s1 = Snake()
s1.eat()
s1.make_sound()
