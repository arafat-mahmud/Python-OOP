from abc import ABC, abstractmethod

class food(ABC):
    @abstractmethod
    def test(self):
        pass
    
class pizza(food):
    def test(self):
        print("Pizza is delicious")

    def size(self):
        print("12-inch pizza")

p1 = pizza()
p1.test()
p1.size()
