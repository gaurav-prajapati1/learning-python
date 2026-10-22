import mysql.connector
from mysql.connector import Error

def get_connection():
    """MySQL Database se connect aur auto-create karne ke liye function"""
    try:
        # Pehle bina database ke server se connect karte hain
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='GauravMySQL@786786'  # Aapka verify kiya hua password
        )
        cursor = connection.cursor()
        
        # 1. Agar school_db nahi bana hai, to use banayein
        cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
        cursor.execute("USE school_db")
        
        # 2. Agar students table nahi bani hai, to use banayein
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                roll_no INT UNIQUE NOT NULL,
                grade VARCHAR(10) NOT NULL
            )
        """)
        cursor.close()
        return connection
    except Error as e:
        print(f"Database se connect nahi ho paya: {e}")
        return None

def insert_student():
    """1. New Student Data Insert karne ke liye"""
    name = input("Student ka Name dalein: ")
    try:
        roll_no = int(input("Roll Number dalein: "))
    except ValueError:
        print("Error: Roll Number sirf ginti (numbers) mein hona chahiye!")
        return
    grade = input("Class/Grade dalein: ")

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO students (name, roll_no, grade) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (name, roll_no, grade))
            conn.commit()
            print("✔ Student data successfully save ho gaya!")
        except Error as e:
            print(f"Error: Data insert nahi hua. (Kya yeh Roll No pehle se hai?): {e}")
        finally:
            cursor.close()
            conn.close()

def display_students():
    """2. Saare Students ka data dekhne ke liye"""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            print("\n--- STUDENT LIST ---")
            print(f"{'ID':<5} {'Name':<20} {'Roll No':<10} {'Grade':<10}")
            print("-" * 50)
            for row in rows:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10}")
            print("-" * 50)
        else:
            print("Database mein abhi koi student nahi hai.")
        
        cursor.close()
        conn.close()

def update_student():
    """3. Student ka data update karne ke liye (Roll Number ke basis par)"""
    try:
        roll_no = int(input("Jis student ka data badalna hai, uska Roll Number dalein: "))
    except ValueError:
        print("Invalid input!")
        return

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
        student = cursor.fetchone()
        
        if not student:
            print("Is Roll Number ka koi student nahi mila.")
            cursor.close()
            conn.close()
            return
            
        print(f"Purana Data -> Name: {student[1]}, Grade: {student[3]}")
        new_name = input("Naya Name dalein (Purana rakhne ke liye Enter dabayein): ") or student[1]
        new_grade = input("Naya Grade dalein (Purana rakhne ke liye Enter dabayein): ") or student[3]
        
        query = "UPDATE students SET name = %s, grade = %s WHERE roll_no = %s"
        try:
            cursor.execute(query, (new_name, new_grade, roll_no))
            conn.commit()
            print("✔ Student data successfully update ho gaya!")
        except Error as e:
            print(f"Update fail ho gaya: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_student():
    """4. Student ka data delete karne ke liye"""
    try:
        roll_no = int(input("Jis student ko delete karna hai, uska Roll Number dalein: "))
    except ValueError:
        print("Invalid input!")
        return

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE roll_no = %s"
        try:
            cursor.execute(query, (roll_no,))
            conn.commit()
            if cursor.rowcount > 0:
                print("✔ Student data successfully delete ho gaya!")
            else:
                print("Is Roll Number ka koi student nahi mila.")
        except Error as e:
            print(f"Delete fail ho gaya: {e}")
        finally:
            cursor.close()
            conn.close()

# Main Program Loop
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Insert Student Data")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student Data")
        print("5. Exit Program")
        
        choice = input("\nApna option chunein (1-5): ")
        
        if choice == '1':
            insert_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Program band ho raha hai. Bye!")
            break
        else:
            print("Galat option! Kripya 1 se 5 ke beech chunein.")

if __name__ == "__main__":
    main()
