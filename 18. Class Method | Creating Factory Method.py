class Student:
    university_name = "Abc"

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):
        print("Name:", self.name, "ID:", self.__id, Student.university_name)

    @classmethod
    def update_name(cls, uni_name):
        cls.uni_name = uni_name

    @classmethod
    def from_string(cls, info):
        name, Id = info.split('-')
        obj = cls(name, Id)
        return obj
    
s1 = Student("Arafat", 23)
s2 = Student.from_string("Mahmud-19")

s1.details()
s2.details()
