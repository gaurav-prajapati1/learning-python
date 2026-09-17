count = 1
while count <= 5:
    print("Hello Sir !")
    count += 1


# WAP to print 100 to 1 number

i = 100

while i >=1:
    print(i)
    i -= 1


# Write the table od any number

num = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(num * i)
    i += 1


# Print the element of the following list using loop

my_list = [10, 20, 30, 40, 50]

for element in my_list:
    print(element)


# Search for a number X in this tuple using loop:
my_tuple = (10, 20, 30, 40, 50)
X = 30

found = False

for element in my_tuple:
    if element == X:
        found = True
        break

if found:
    print("Number found")
else:
    print("Number not found")


# BREAK : its terminate the loops and exit the any condition

i = 1
while i <= 5:
    print(i)
    if(i ==  3):
        break
    i += 1


# CONTINUE : Terminates execution in the current interation and continue execution of te loop with the next interation

i = 1
while i <= 10:
  if (i % 2 == 0):
    i += 1
    continue
  print (i)
  i += 1


# FOR loops : when we know how many times we execute the interation
# 1. SYNTAX:

# for var_name in list:
# #   Some Work

# # 2. SYNTAX
# for var_name in list:
# #   Some Work
# else :
# #   Some Work


# EXAMPLE:

tup = (1,2,3,4,5,6,7,8,9,10)
for num in tup:
  print(num)


# FOR STRING
string = "GAURAVPRAJAPATI"
for char in string:
    print(char)


# WAP Print the element of the following list using loop
num  = [1,4,9,16,25,36,49,64,81,100]
for element in num:
   print(element)


# Search for a number X in this tuple using loop:

num = (1,4,9,16,25,36,49,64,81,100)
key = 81
i = 0
for element in num:
    if (key == element):
        print(i)
    i+=1
else:
    print("NOT Found")


# RANGE() : Range function returns a sequence of number , starting from 0 by default, and increment  by 1 (by default), and stops before a specified number

# # SYNTAX :
# range(start?, stop, step)

# # EXAMPLE:
# for i in range(1,10,1):
#     print(i)


# WAP to Print 1 to 100

for i in range (1,101):
    print(i)


# WAP to Print 100 to 1

for i in range (100,0,-1):
    print(i)




# WAP Print the multuplication table of a number

num = int(input("Enter the number: "))
for i in range (1,11):
    print(num*i)




# WAP to find the sum of first n natural number
num = int(input("Enter the number: "))
sum = 0
for i in range (1, num+1):
    sum = sum + i
    print("The SUM is = ",sum)




# WAP to find the factorial of first n number
num = int(input("Enter the number: "))
fact = 1
for i in range (1,num+1):
    fact = fact * i
    print("Factorial is =",fact)
