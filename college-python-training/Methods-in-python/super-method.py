class Car:
    def __init__(self, type):
        self.type = type
        @staticmethod
        def start():
            print("car started")
class Toyotacar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
car1 = Toyotacar("perius", "deisel")
print(car1.name)
print(car1.type)