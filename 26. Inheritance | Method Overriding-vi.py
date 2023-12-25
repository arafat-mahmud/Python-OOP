class A:
    def __init__(self):
        print("__init__of class A")

    def method_1(self):
        print("speaking")

    def method_2(self):
        print("reading")

class B(A):
    def __init__(self):
        pass

    def method_1(self):
        super().method1()
        print("listing")

b1 = B()
b1.method_1()
b1.method_2()
