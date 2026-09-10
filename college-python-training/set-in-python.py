# collection = {1,4,6,8,10}
# print(collection)
# print(type(collection))


# # Use the function 

# # print(collection.add(5))
# # print(collection.remove(1))

# # USE the UNION fucntion 
# a = {1,2,3,4}
# b = {5,6,7}
# print(a.union(b))



# # USE the INTERSECTION fucntion

# a = {1,2,3,4}
# b = {3,4,8,9}
# print(a.intersection(b))




# dict = {
#     "cat":"a small animal",
#     "table":("a piece of furniture","list of fact")
# }
# print(dict)



# WAP to enters marks of 3 subjects from the user and store them in a dict. Start an empty dict & add on by one

# marks = {}
# marks["Maths"] = int(input("Enter Maths marks: "))
# marks["Physics"] = int(input("Enter Physics marks: "))
# marks["Chemistry"] = int(input("Enter Chemistry marks: "))

# print(marks)



# For another type same program 

mark = {}
x = int(input("Enter PHY: "))
mark.update({"PHY": x})
x = int(input("Enter Maths: "))
mark.update({"Maths": x})
x = int(input("Enter CHEM: "))
mark.update({"CHEM": x})

print(mark)


