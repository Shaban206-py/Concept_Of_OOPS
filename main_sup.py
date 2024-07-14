#Super() Method
'''
super() method is use to access method from parent class
'''




class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Supra", "Hybrid")   
print(car1.name)     
print(car1.type)
