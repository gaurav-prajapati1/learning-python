class Animal:
    def sound(self):
        print("Animal make sounds ")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dogs Barks")
    
obj = Dog()
obj.sound()