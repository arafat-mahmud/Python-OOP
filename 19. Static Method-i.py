class Student:
    university_name = "Abc"

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id
        
    def details(self):
        print("Name:",  self.name, "ID", self.__id, Student.university_name)
        
    @classmethod
    def update_university_name(cls, uni_name):
        cls.university_name = uni_name
        
    @staticmethod
    def check_department(Id):
        if Id[3:5] == "01" : print("CSE")
        elif Id[3:5] == "41" : print("CS")
        
        
Student.check_department("123134")
# s1 = Student("Arafat", 23)
# s2 = Student("Mahmud")
# s1.details()
# s2.details()
Student.check_department("5323432")