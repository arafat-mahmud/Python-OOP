class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self, num, clr):
        num = num + 5 #60
        clr1 = clr
        clr1[0] = "Brown"
        print("Method inside:", num)
        print("Method inside:", clr1)

colors = ["Black", "Red", "Yellow", "Blue"]
c1 = Cat("White", "jumping")

x = 55

c1.view(x, colors)

print("Method outside", x)
print("Method outside", colors)
