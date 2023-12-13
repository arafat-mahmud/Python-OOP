class Student:
    def __init__(self, name, age):
        self.name = name    #instance variable
        self.age = age      #instance variable
        #print("a student object created")


#======== Object/data manipulate ===========
#create an instance of the class 'Student' with values for attributes (name and age).
#passing arguments to the constructor.

s1 = Student("Arafat", 19)
s2 = Student("Mahmud", 23)

print("Previous age: ",s1.age)

s1.age = 20 #update age s1
# s2.age = 24 
    #update age s2

print(s1.name, s1.age)  # 20 age
print(s2.name, s2.age)

