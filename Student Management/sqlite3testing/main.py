import sqlite3

conn = sqlite3.connect("Student Management/sqlite3testing/practice.db")

cursor=conn.cursor()

def addStudent():   
    name = input("What is the your name: ")
    age = int(input("What is the your age:"))
    course = input("Input your course: ")
    cursor.execute(f"""INSERT INTO student (studentid, name, age, course)
                   VALUES 
                   (2026000, "{name}", {age}, "{course}")""")
    
addStudent()

conn.commit()
conn.close()