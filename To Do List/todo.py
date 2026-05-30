input("To-do list 1.0\nPress to continue..")
todo=[]

def createTask():
    x=input("Task: ")
    todo.append(x)
    input(f"Created:{x}\nPress to continue..")

def deleteTask():
    x=input(f"Choose 1-{len(todo)}: ")
    if int(x) <= len(todo):
        print(f"Removed {todo[x]}")
        todo.pop(int(x))
    else:
        input(f"Must be within 1-{len(todo)}\nPress anything to continue..")

def viewTasks():
    for i in todo:
        input(f"-{i}\nPress to anything to continue..")
        
while True:

    userInput=input("1.Add a task\n2.Remove a task\n3.View tasks\n4.Exit\nChoose option: ") 

    if int(userInput)==1:
        createTask()
        continue
    elif int(userInput)==2:
        deleteTask()
        continue
    elif int(userInput)==3:
        viewTasks()
        print(userInput)
        continue
    elif userInput=="4":
        break
    else:
        print("its broken")
        continue