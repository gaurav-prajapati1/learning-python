# Class is a blueprint for creating a object 

# Creating a class 

# class Students:
#     name = "Gaurav Prajapati"

# # Creating a object (instance)
# S1 = Students()
# print(S1.name)



# Constructor is aslo known as init function
# class Student:
#     def __init__(self,fullname):
#         self.name = fullname
# S1 = Student("Gaurav Prajapati")
# print(S1.name)



# class Student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
# S1 = Student("Gaurav",97)
# print(S1.name,S1.marks)

# S2 = Student("Piyush",100)
# print(S2.name,S2.marks)



# Methods are functions that belong to objects;

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#     def hello(self):
#      print("Hello", self.name)

# # Class create 

# S1 = Student("Gaurav Prajapati")
# S1.hello()


# Create Studet class that takes name and marks of 3 subject as argument in constructor . Then create a method to print the average 
class Student:
    def __init__(self,name,marks):
      self.name = name
      self.marks = marks
    def get_avg(self):
      sum = 0
      for val in self.marks:
       sum += val
      print("Hi", self.name,"Your avg is: ",sum/3)
S1 = Student("Vijay Mallya",[70,86,76])
S1.get_avg()