class Student:

    def __init__(self, **info): # Unknown number, what (**info)
        if len(info) == 3:
            self.name = info['name']
            self.id = info['id']
            self.grade = info['grade']
            
        elif len(info) == 2:
            self.name = info['name']
            self.id = info['id']

        elif len(info) == 1:
            self.name = info['name']

        print("A student is created")


s1 = Student(name = "Arafat", id = 23, grade = 4.0)
s2 = Student(id = 19, name = "Mahmud")
s3 = Student(name = "Sidra")
s4 = Student()
