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

def tCreation():
    task_name = input("Task Name: ")
    _task = Task(task_name)

    user_data["todos"].append(
        {
            "task": _task.task,
            "done": _task.done
        }
    )

    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)
        
def listTask():
    for i in user_data["todos"]:
        print(i)
        
while running:
    print("1.Create a task\n2.List all task\n3.Clear all completed task\n4.Mark task as completed")
    input("Enter:")
    
    if input == 1:
        tCreation()
    if input == 2:
        listTask()
    else:
        print("Unknown...")