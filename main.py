#import sys
import json
#import uuid
from prettytable import PrettyTable
import os
from itertools import count

def idCount():
  with open('Todo.json', "r") as f:
    data = json.load(f)
    if not data: #check if the list is empty ie. a new user/todo list
      id = 0
    else:
      id = max(item["id"] for item in data)
    counter = count(id + 1)
    #print(counter)
  return next(counter) #returns an integer

def menu():
  menu = ("Select one of the following options by entering the option number: \n"
    "1. Add an item \n"
    "2. Remove an item \n"
    "3. View item list \n"
    "4. Update task status \n"
    "5. Exit \n")
  print(menu)

def createJSON():
  filename = "Todo.json"
  if not os.path.exists(filename):
    with open(filename, "w") as file: #If file doesn't exist, create the file
        data = []  #start with an empty list
        json.dump(data, file, indent=4)

def writeJSON(task):
  filename = "Todo.json"

  # Create new task data
  input_data = {
    "id": int(idCount()),#str(uuid.uuid4()),
    "Task": task,
    "Status": "Pending"
  }

  # Ensure the file exists and has valid JSON content
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as file:
      data = json.load(file)  # Load existing data
  else:
    data = []

  # Append new task
  data.append(input_data)

  #print("Updated Data:", json.dumps(data, indent=4))

  # Write updated data back to JSON file
  with open(filename, "w") as file:
    json.dump(data, file, indent=4)

  print("Task \"" + str(input_data["Task"]) + "\" added to list \n\n")

def removeJSON(a):
  with open('Todo.json', "r") as f:
    data = json.load(f)
  
  # Find the index of the item where id = user_input
  item_to_remove = next((i for i, item in enumerate(data) if item["id"] == int(a)), None)

  # If the item with id = 4 is found, pop it
  if item_to_remove is not None:
    data.pop(item_to_remove)
  
  # Write updated data back to JSON file
  with open('Todo.json', "w") as file:
    json.dump(data, file, indent=4) 
  
  print("Item id " + a + " Removed from List")
  #menu()

def add(add_item):
  writeJSON(add_item)
  #print("New item added: " + add_item + "\n")
  menu()

def delete(delete_item):
  removeJSON(delete_item)
  #print("Item deleted: " + delete_item + "\n")  
  menu()

def updateStatus(updateStatusID):
  status = "Complete"
  updateStatusID = int(updateStatusID)
  print(updateStatusID)
  with open('Todo.json', "r") as f:
    data = json.load(f)
  
  updated = False
  for item in data:
    if item["id"] == updateStatusID:
      item["Status"] = status
      updated = True
  
  if updated:
    with open('Todo.json', "w") as file:
      json.dump(data, file, indent=4)
    print("Item id " + str(updateStatusID) + " Status updated to " + status)
  else:
    print("ID not found")
  menu()

def list():
  #table = PrettyTable(["ID", "Task", "Status"])

  with open('Todo.json', "r") as f:
    data = json.load(f)
  
  table = PrettyTable()

  table.field_names = data[0].keys()

  for item in data:
    table.add_row(item.values())

  print(table)
  #menu()

def main():
  welcome = ("Welcome to the Todo list app. \n\n")
  print(welcome)
  createJSON() # if file doesnt exist, create the file
  menu()
  #print(menu)
  while True:
    
    user_input = input()
    
    match user_input:
      case '1':
        print("Type in an item to add to the list: ")
        new_item = input()
        add(new_item)
      case '2':
        list()
        print("Type the ID of the item to remove it from the list: ")
        remove_item = input()
        delete(remove_item)
      case '3':
        print("See the list of items below: ")
        list()
        menu()
      case '4':
        list()
        print("Type the ID of the item to update its status: ")
        updateStatusID = input()
        updateStatus(updateStatusID)
      case '5':
        print("Exiting Todo List")
        break
      case _:
        print("Your input was not recongnised: ")
        menu()
    #print(user_input)
if __name__ == '__main__':
  main()