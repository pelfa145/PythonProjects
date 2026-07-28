quitMenu = 0

def removeStudent():
    printRecords()
    choice = input("From top to bottom 1-"+str(len(freshmen))+": ")
    choice = int(choice)
    choice -= 1
    freshmen.pop(choice)

def printRecords():
    print("ID|Name|Age|Course\n=======================")
    if len(freshmen) < 1:
        print("STUDENT RECORDS IS EMPTY")
    else:
        for i in freshmen:
            print(f"{i["studentid"]}|{i["studentname"]}|{i['age']}|{i['course']}")
#print(f"=========\nName: {i["studentname"]}\nAge: {i["age"]}\nCourse: {i["course"]}\nStudent ID: {i["studentid"]}\n=========")

def addStudent():
    studentName = input("What's your name?: ")
    age = input("How old are you?: ")
    course = input("What course?: ")
    studentID=input("What's your student id?: ")
    listappend = {"studentid":studentID, "course": course, "age": age, "studentname": studentName}
    freshmen.append(listappend)

def showMenu():
    while True:
        print("Student Manager!\n1. Add a student\n2. Remove a student\n3. Show records\n4. Quit")
        choice = input("Choose an option 1-4: ")
        match choice:
            case "1":
                return addStudent()
            case "2":
                removeStudent()
            case "3": 
                printRecords()
                input("=======================\nPress anything to continue..")
            case "4":
                break

    
    

freshmen = [
    {
    "studentid":"0001",
    "course":"BSIT",
    "age":18,
    "studentname":"Jadon Cyrus Paran",
    }, 
    
]




showMenu()

