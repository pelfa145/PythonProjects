import sqlite3
import pandas as pd

conn = sqlite3.connect("practice.db")
conn.row_factory = sqlite3.Row 
cursor=conn.cursor()


def StudentIDasList():
    df = pd.read_sql_query("SELECT studentid FROM student", conn)
    studentids = df['studentid'].tolist()
    return studentids

def addStudent():
    studentids = StudentIDasList() 
    try:
        studentid = int(studentids[len(studentids)-1])
    except:
        name = input("Input student's name: ")
        age = input("Input student's age: ")
        course = input("Input student's course: ")
        cursor.execute("""INSERT INTO student (studentid,name,age,course)
                        VALUES (?,?,?,?)""",(2026000, name, age, course, ))
        conn.commit()
        print(f"Added {name.split()[0]} in students")
        return
    studentid += 1
    
    name = input("What is the your name: ")
    age = int(input("What is the your age:"))
    course = input("Input your course: ")
    cursor.execute("""INSERT INTO student (studentid, name, age, course)
                   VALUES 
                   (?, ?, ?, ?)
    """, (studentid, name, age, course))
    conn.commit()
    print("Added student successfully.")
    
def removeStudent():
    studentid = int(input("Input Student ID:"))
    cursor.execute("DELETE FROM student WHERE studentid = ?",(studentid,))
    conn.commit()
    print("Student deleted.")
    
def viewAllStudents():
    cursor.execute("SELECT * FROM student")
    
    rows = cursor.fetchall()
    
    studentlists = [dict(row) for row in rows]
    #print(studentlists)
    for student in studentlists:
        print(f"ID: {student['studentid']} | Name: {student['name']} | Course: {student['course']}")
    
    
    
    
    
def showMenu():
    while True:
        print("Student Management w/ SQL 1.0\n1. Add student\n2. Remove a student\n3. View all students\n4. Exit")
        choice = int(input("Choose an option 1-4: "))
        match choice: 
            case 1: 
                addStudent()
                continue
            case 2:
                removeStudent()
                continue
            case 3: 
                viewAllStudents()
                continue
            case 4: 
                break

showMenu()


conn.close()