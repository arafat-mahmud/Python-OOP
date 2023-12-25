class Engine:
    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print("Engine is started")

    def stop(self):
        print("Engine is stopped")

class Car:
    def __init__(self ,name,cc):
        self.name = name
        self.engine = Engine(cc)

    def run(self):
        #print(self.engine)
        self.engine.start()
        print("Car is running")

c1 = Car("BMW", 2000)
c1.run()