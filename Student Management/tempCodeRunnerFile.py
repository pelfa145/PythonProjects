quitMenu = 0

def searchStudent(studentid):
    b=0
    for i in freshmen:
        if studentid == i['studentid']:
            print(f"Found! \n====================\nStudent: {i['studentname']}\nAge: {i['age']}\nCourse: {i['course']}\nStudent ID: {i['studentid']}\n====================")
            input("Press anything to continue...")
            return b
        else: b+=1                  
    return -1    

def editStudent(studentIndex):
    
    print("What do you want to update?\n1. Name\n2. Age\n3. Course\n4. Quit\n")
    choice = input("Choice: ")
    match choice:
        case "1":
            change = input("New name: ")
            freshmen[studentIndex]['studentname'] = change
            print(freshmen[studentIndex])
            return 1
        case "2":
            change = input("New age: ")
            freshmen[studentIndex]['age'] = change
            return 2
        case "3":
            change = input("New course: ")
            freshmen[studentIndex]['course'] = change
            return 3
        case "4":
            return 0

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
        print("Student Manager!\n1. Add a student\n2. Remove a student\n3. Show records\n4. Search Student\n5. Modify student details\n6. Quit")
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
                x=input("Student ID of Student: ")
                result = searchStudent(x)
                if result == 0:
                    input(f"No student was found with Student ID: {x}\nPress enter to continue...")
            case "5":
                x=input("Student ID of Student: ")
                result = searchStudent(x)
                if result == -1:
                    input(f"No student was found with Student ID: {x}\nPress enter to continue...")
                else: editStudent(result)
                if editStudent == 0:
                    input("No changes we're made, press enter to continue..")
                elif editStudent == 1:
                    input("Changed Student name.")
                elif editStudent == 2:
                    input("Changed Student age.")
                elif editStudent == 3:
                    input("Changed Student course.")
                
            case "6":
                break
    
    

freshmen = [
    {
    "studentid":"2026000",
    "course":"BSIT",
    "age":18,
    "studentname":"Jadon Cyrus Paran",
    }, 
    {
        "studentid": "2026001",
        "studentname": "John Doe",
        "age": 19,
        "course": "BSIT"
    },
    {
        "studentid": "2026002",
        "studentname": "Jane Smith",
        "age": 18,
        "course": "BSCS"
    },
    {
        "studentid": "2026003",
        "studentname": "Michael Santos",
        "age": 20,
        "course": "BSIT"
    },
    {
        "studentid": "2026004",
        "studentname": "Sarah Cruz",
        "age": 19,
        "course": "BSIS"
    },
    {
        "studentid": "2026005",
        "studentname": "David Reyes",
        "age": 21,
        "course": "BSCpE"
    },
    {
        "studentid": "2026006",
        "studentname": "Angela Flores",
        "age": 18,
        "course": "BSIT"
    },
    {
        "studentid": "2026007",
        "studentname": "Joshua Garcia",
        "age": 20,
        "course": "BSCS"
    },
    {
        "studentid": "2026008",
        "studentname": "Nicole Mendoza",
        "age": 19,
        "course": "BSIT"
    },
    {
        "studentid": "2026009",
        "studentname": "Ethan Ramos",
        "age": 22,
        "course": "BSECE"
    },
    {
        "studentid": "2026010",
        "studentname": "Sophia Villanueva",
        "age": 18,
        "course": "BSIS"
    }
]

showMenu()

