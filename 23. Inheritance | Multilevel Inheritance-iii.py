class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id

    def details(self):
        print("Name:", self.name, "ID:", self.id)

class CSE_Student(Student):     # Parent class
    def __init__(self, name, Id, labs):
        super().init__(name, Id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE student is crying because of", 
              self.no_of_labs, "labs")
        
class CSE_Freshers(CSE_Student):       # Child class
    def enroll_CSE110(self):
        print("All day party")


s1 = CSE_Student("Arafat", 23, 3)      # name, Id, labs
s2 = CSE_Freshers("Mahmud", 19)

s1.details()
s2.details()

s1.cry()
