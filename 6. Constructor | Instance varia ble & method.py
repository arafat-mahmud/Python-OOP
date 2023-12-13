class Dog:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):      # Update the dog's color
        self.color = color

    def poke(self):
        print(self.color, self.name, "is attacking")


d1 = Dog("dog arafat", "Black")
d2 = Dog("dog mahmud", "white")

# d1.poke()
d1.update_color("Brown")
d1.poke()

# print(d2.__dict__)
# print(d1.__dict__)

# print(dir(d1))

