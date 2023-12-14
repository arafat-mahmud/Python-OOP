class Student:

    def __init__(self, name, Id):
        self.name = name         # instance variable
        self.__id = Id           # private instance variable

    def details(self):           # instance method
        print("Name:", self.name, "ID:", self.__id)

    def update_id(self, Id):
        if(Id > 0):
            self.__id = id
        else:
            print("Invalid ID, Try again please.")

s1 = Student("Arafat", 23)
s2 = Student("Mahmud", 19)

s1.update_id(-999)

s1.details()
s2.details()
