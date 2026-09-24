# del keyword is used to delete properties or object itself

# Synatx :
# del S1.name
# del S1

# example:
class Student:
    def __init__(self,name):
        self.name = name 
S1 = Student("Gaurav Prajapati")
del S1.name
print(S1.name)

