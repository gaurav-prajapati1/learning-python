import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPass"
)

cursor = db.cursor()

# Create Bank database
cursor.execute("CREATE DATABASE IF NOT EXISTS Bank")

# Use Bank database
cursor.execute("USE Bank")

# Create account table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS account (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        balance DECIMAL(10, 2)
    )
""")

print("Bank database and Account table ready")

# sql = "INSERT INTO account (name, balance) VALUES (%s, %s)"

# data = [
#     ("Gaurav", 50000),
#     ("Rahul", 25000)
# ]

# cursor.executemany(sql, data)
# db.commit()

# print("2 account details inserted")

cursor.execute("SELECT * FROM account")

data = cursor.fetchall()

for account in data:
    print(account)


cursor.close()
db.close()