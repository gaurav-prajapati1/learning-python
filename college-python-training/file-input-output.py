# Create any new file

# f = open("File_name.py", "w")
# f.write("this is a new line")
# f.close()


# Read any file
# f = open("dictionary.py","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# For deleteing any file

# import os
# os.remove("File_name.py")

# WAP Create the new file "practice.txt" using python. Add the following data in it

# f = open("File_name.py", "w")
# f.write("Hello Everyone\nWe are learning File I/O, using\nI love programming in Java")
# f.close()


# WAP read the file using java with python in abve file

f = open("File_name.py","r")
data = f.read()
new_data = data.replace("Java","Python")
print(new_data)
f = open("File_name.py", "w")
f.write(new_data)
