class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house has", self.window, "window and", self.door, "door")

h1 = House(6, 2)
h2 = House(4, 1)

h1.view()
h2.view()
