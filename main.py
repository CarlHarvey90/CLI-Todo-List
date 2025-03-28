#import sys
import json
#import uuid
from prettytable import PrettyTable
import os
from itertools import count

def idCount():
  with open('Todo.json', "r") as f:
    data = json.load(f)
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
    data = []  # If file doesn't exist or is empty, start with an empty list

  # Append new task
  data.append(input_data)

  # Debugging: Print data before writing
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
  #print(item_to_remove) 
  #print("hello")

  #print(data["id"][int(item_to_remove)])

  #if item_to_remove in data:
  # remove_id = data.pop("id"[item_to_remove])
  

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
  menu()
  #print(menu)
  while True:
    
    user_input = input()
    
    if user_input == '5':
      print("Exiting Todo List")
      break
    
    if user_input == '1':
      print("Type in a item to add to the list: ")
      new_item = input()
      add(new_item)
    
    if user_input == '2':
      list()
      print("Type the ID of the item to remove it from the list: ")
      remove_item = input()
      delete(remove_item)

    if user_input == '3':
      print("See the list of items below: ")
      list()

    if user_input == '4':
      list()
      print("Type the ID of the item to update its status: ")
      updateStatusID = input()
      updateStatus(updateStatusID)

    #print(user_input)
if __name__ == '__main__':
  main()