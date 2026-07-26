
#To Do List Version 2!!!
class task:
    def __init__(self, description, status):
        self.description = description
        self.status = bool(status)
        
        
    
class ToDoList:
    def __init__(self):
        self.list = []
        
    def addTask(self, description, status):
        newTask = task(description, status)
        self.list.append(newTask)
        self.status = bool(status)
        status_text = "Done" if status else "Pending"
        print(f"Added: {description} [{status_text}]")
        
    def showToDo(self):    
        for i in self.list:
            status_text = "Done" if i.status else "Pending"
            print(f"- {i.description} [{status_text}]")
            
    def removeTask(self, choice):
        found = False
        for i in self.list:
            if i.description.lower() == choice.lower():
                self.list.remove(i)
                print(f"Removed {i.description}.")
                found=True
                break 
            if not found:
                print("Task not found.")
        
    def markDone(self, task_name):
        found = False
        for i in self.list:
            if i.description.lower() == task_name.lower():
                i.status = True
                print(f"Marked '{i.description}' as Done!")
                found = True
                break
        
        if not found:
            print("Task not found.")

todo = ToDoList()

def showMenu():
    choice = ''
    while not choice == '5':
        print("---To Do List V2---\n1. Add a task\n2. Show To Do List\n3. Mark a task done\n4. Remove a task\n5. Quit")
        choice = input("Choose an option 1-4: ").strip()
        match choice:
            case '1':
                x=input("Whats the description of your task: ")
                while True:
                    y=input("Status of your task (Pending/Done): ")
                    y = y.capitalize()
                    if y == "Done": 
                        y = True
                        break
                    elif y == "Pending":
                        y = False
                        break
                    else:
                        print("Pending or done only")
                todo.addTask(x, y)
            case '2':
                todo.showToDo()
                input("Press to continue...")
            case '3':
                todo.showToDo()
                x = input("Name the task you want to mark done: ").strip()
                todo.markDone(x)
            case '4':
                todo.showToDo()
                x = input("Name the task you want to remove: ").strip()
                todo.removeTask(x)
            case '5':
                print("Goodbye")
            case _:
                print("\nInvalid choice. Enter an option between 1-5.")
                

showMenu()
    
