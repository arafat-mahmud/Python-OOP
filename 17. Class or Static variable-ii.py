class Student:
    university_name = "ABC"

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):
        print("Name:", self.name, "ID:", self.__id, Student.university_name)

    @classmethod
    def up_university_name(cls, uni_name):
        cls.university_name = uni_name  # Get 2 no line(university_name)

s1 = Student("Arafat", 23)
s2 = Student("Mahmud", 19)

s1.details()
s1.details()

Student.up_university_name("Oxford")
s1.details()
s2.details()
