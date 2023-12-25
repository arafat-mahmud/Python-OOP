from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass

class B(A):
    @abstractmethod
    def method2(self):
        pass

class C(B):
    def method1(self):
        print("Method1 is overring")

    def method2(self):
        print("Method2 is overring")

c1 = C()
c1.method1()
c1.method2()