print("Hello! its time for you to write up yo grades")
print("HELL YEAHHH")
sbj = ["English", "Computer", "Filipino", "Science", "Math"]
grades = {}
num = 0


def inputGrade():
    for i in sbj:
        grade = input(f"Input your grades in {i}: ")
        grade = int(grade)
        if grade > 100:
            print("1-100 Only")
            break
        grades[f"{i}"] = [grade]


def viewGrades():
    print("Subject  Grades")
    for key, value in grades.items():
        print(f"{key}: {value}")
    input("Press any key to continue...")

def modifyGrade(subject):
    subject = 

while True:

    print("==========GRADE TRACKER==========")
    print("1. Input Grades")
    print("2. View Grades")
    print("3. Modify Grades")
    print("4. Exit")
    choice = input("Choose an option 1-4: ")
    choice = int(choice)
    if choice == 1:
        inputGrade()
        continue
    elif choice == 2:
        viewGrades()
    elif choice == 3:
        for i in grades.items():
            num += 1
            print(f"{num}.{i}")
        option = input(f"Choose what subject: 1 - {len(grades.items())}:")
        option = int(option)
    elif choice == 4:
        print("Bye")
    else:
        print("Choose between 1-4")
        continue
