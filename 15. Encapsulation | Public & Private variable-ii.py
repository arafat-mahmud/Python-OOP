class Student:

    def __init__(self, name, Id):
        self.name = name    # # instance variable
        self.__id = Id      # private instance variable

    def details(self):      # # instance method
        print("Name:", self.name, "\nID:", self.__id)
        self.__method()

    def __method(self):
        print("Private method executed.")


s1 = Student("Arafat", 23)
s2 = Student("Mahmud", 19)

# s1.__method()

s1.details()
