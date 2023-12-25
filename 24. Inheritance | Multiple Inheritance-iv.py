class A:
    def __init__(self):
        print("__init__of class A")

    def method_1(self):
        print("Method_1 of class A")

class B:
    def __init__(self):
        print("__init__of class B")

    def method_1(self):
        print("Method_1 of class B")

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("__init__of class C")

    def metho2(self):
        print("Method_2 of class C")

c1 = C()
c1.method_1()
B.method_1(c1)
