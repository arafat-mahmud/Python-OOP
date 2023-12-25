class Student:
    def __init__(self, name, id):
        self.name = name
        self.ID = id

    def __str__(self):
        return "My name is " + self.name

s1 = Student("Bob", 22)
s2 = Student("Carol", 77)
print(s1)
print(s2.__str__())
