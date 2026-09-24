# Inheritence in OOps
# When one class (child/derived) derives the properties and methods of another class (parent/base)

# example:


# class Car:
#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car Stopped")


# class Toyotacar(Car):
#     def __init__(self, name):
#         self.name = name


# car1 = Toyotacar("Fortuner")
# print(car1.name)
# print(car1.start())
# print(car1.stop())

# Example:


class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):
    varC = "Welcome to class C"


C1 = C()
print(C1.varA)
print(C1.varB)
print(C1.varC)
