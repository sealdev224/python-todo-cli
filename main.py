import json
from colorama import Fore, Style

class Task:
    def __init__(self, task, done=False):
        self.task = task
        self.done = done
        
    def complete(self):
        self.done = True
        


try:
    with open("user_data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
 
    print("What is your name?")
    name = input("Name: ")
 
    user_data = {
        "name": name,
        "todos": [
         
        ]
    }
 
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)
except:
    print("Error...???")

running = True

print("Create a task")
input("Name: ")