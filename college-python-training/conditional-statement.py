# IF STATEMENT 

#a = 10
#if a % 2 == 0:
#    print("Even Number")

# IF-ELSE STATEMENT 

# a = 10
# if a % 2 == 0:
#	print("Even")

# else: print("Odd")



# IF - ELIF ELSE STATEMENT 

# per = int(input("Enter your marks: "))
# if per >= 60:
# 	print("First Div")
# elif per >= 35:
# 	print("Second Div")
# elif per >= 25:
# 	print("Third Div")
# else : 
# 		print("Fail")



# NESTED IF ELSE STATEMENT


# age = int(input("Enter your age: "))
# if(age >= 18):
#     if(age >= 80):
# 	    print("Can not Drive")
#     else : 
#         print ("Can Drive ")
# else :
#     print ("Your age cannot  modify")



# write a program to check number is divisible by 3 and 5 

# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by both 3 and 5.")
# else:
#     print("The number is not divisible by both 3 and 5.")




# Write a program to  find the lasgest number 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
