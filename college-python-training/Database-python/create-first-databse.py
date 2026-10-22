import mysql.connector 
 
db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="YourPass" 
) 
 
cursor = db.cursor() 
 
cursor.execute("CREATE DATABASE IF NOT EXISTS SAITM") 
cursor.execute("USE SAITM") 
 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS student_data ( 
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(100), 
        age INT, 
        email VARCHAR(100) 
    ) 
""") 
 
print("SAITM database ready") 
 
# Student data INSERT nahi hoga baar-baar
# sql = "INSERT INTO student_data (name, age, email) VALUES (%s, %s, %s)"
# data = [ 
#     ("Rahul", 20, "rahul@gmail.com"), 
#     ("Priya", 21, "priya@gmail.com"), 
#     ("Amit", 19, "amit@gmail.com"), 
#     ("Sneha", 22, "sneha@gmail.com"), 
#     ("Rohit", 20, "rohit@gmail.com") 
# ]
# cursor.executemany(sql, data)
# db.commit()

# cursor.execute(""" 
#     UPDATE student_data 
#     SET name = 'Gaurav Prajapati' 
#     WHERE id = 1 
# """) 
 
db.commit() 

cursor.execute("SELECT * FROM student_data") 
 
data = cursor.fetchall() 
 
for student in data: 
    print(student) 
 
cursor.close() 
db.close()