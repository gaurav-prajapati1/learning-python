#  SYNTAX : dict = {key_name : value, key : value}

dict = {
    "name" : "Gaurav Prajapati",
    "CGPA" : 0.0 ,
    "marks" : [10,20,30],
}

gaurav = {
    "name" : "Gaurav",
    "CGPA" : 9.6 ,
    "marks" : [10],
}

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
print(dict.pop("marks"))

print(dict.update(gaurav))
