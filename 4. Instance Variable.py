class House:
    def __init__(self):
        self.room = 4    #instance variable
        self.window = 8   #instance variable
        self.door = 6     #instance variable

    def view(self):
        """A method to display the house's features"""
        print("Room:", self.room, ", Windows:", self.window,  ", Door:", self.door)

h1 = House()
print("House h1 has: ")

h1.door = 7 #update
h1.view()