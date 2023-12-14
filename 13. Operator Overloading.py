class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house has", self.window, "window and", self.door, "door")

    def __add__(self, other):
        new_windows = self.windows + other.windows
        new_doors = self.doors + other.doors  #return "new house has "+str(new_windows)+" windows and "+str(new_doors)+" doors"
        obj = House(new_windows,new_doors)
        return obj


h1 = House(6,3)
h2 = House(8,2)
h1.views()
h2.views()
h3 = h1 +h2
h3.views()

#print(h1 + h2)
