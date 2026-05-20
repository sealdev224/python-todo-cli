import json

class Task:
    def __init__(self, task, done=False):
        self.task = task
        self.done = done
        
    def complete(self):
        self.done = True
        


try:
    with open("user_data.json", "r") as file:
        data = json.load(file)
    user_data = data
except FileNotFoundError:
 
    print("What is your name?")
    name = input("Name: ")
 
    user_data = {
        "name": name,
        "todos": [
         
        ]
    }
 
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)
except:
    print("Error...???")

running = True

def dumpJSON():
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

def tCreation():
    task_name = input("Task Name: ")
    _task = Task(task_name)

    user_data["todos"].append(
        {
            "task": _task.task,
            "done": _task.done
        }
    )

    dumpJSON()
        
def listTask():
    for i in user_data["todos"]:
        print(f"The task {i['task']} completion state is: {i['done']}")
        
def resetList():
    user_data["todos"] = []
    dumpJSON()

def whichTask():
    listTask()
    print("Which task would you like to mark as completed? | info: index number starts at 1?")
    completedChoice = input("Enter: ")
    completedChoice = int(completedChoice.strip())
    completedChoice -= 1
    user_data["todos"][completedChoice]["done"] = True
    dumpJSON()

def delTask():
    listTask()
    print("Which task would you like to delete the | info: index number starts at 1?")
    completedChoice = input("Enter: ")
    completedChoice = int(completedChoice.strip())
    completedChoice -= 1
    user_data["todos"].pop(completedChoice)
    
    dumpJSON()


        
while running:
    print("1.Create a task\n2.List all task\n3.Clear all completed task\n4.Mark task as completed\n5.Delete task")
    choice = input("Enter:")
    choice = int(choice.strip())
    
    if choice == 1:
        tCreation()
    if choice == 2:
        listTask()
    if choice == 3:
        resetList()
    if choice == 4:
        whichTask()
    if choice == 5:
        delTask()