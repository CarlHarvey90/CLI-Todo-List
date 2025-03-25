import sys
import json
import uuid
import os

def menu():
  menu = ("Select one of the following options by entering the option number: \n"
    "1. Add an item \n"
    "2. Remove an item \n"
    "3. View item list \n"
    "4. Exit \n")
  print(menu)

def writeJSON(a):
  filename = "Todo.json"
  input_data = {} 
  input_data["id"] = str(uuid.uuid4())
  input_data["Task"] = a
  input_data["Status"] = "Pending"

  # Check if the file exists and read existing data
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as file:
      try:
        data = json.load(file)  # Load existing data
        if not isinstance(data, list):
          data = []  # Ensure data is a list
      except (json.JSONDecodeError, TypeError):
        data = []  # Handle empty or invalid JSON file
  else:
        data = []

  # Append new user data
  data.append(input_data)

  with open("Todo.json", "w") as file:
        json.dump(data, file, indent=4)

  print("write to JSON")

def removeJSON(a):
  print("Remove from JSON")

def add(add_item):
  writeJSON(add_item)
  print("New item added: " + add_item + "\n")
  menu()

def delete(delete_item):
  removeJSON(delete_item)
  print("Item deleted: " + delete_item + "\n")  
  menu()

def list():
  #print("New item added: " + add_item)
  menu()

def main():
  welcome = ("Welcome to the Todo list app. \n\n")
  print(welcome)
  menu()
  #print(menu)
  while True:
    
    user_input = input()
    
    if user_input == '4':
      print("Exiting Todo List")
      break
    
    if user_input == '1':
      print("Type in a item to add to the list: ")
      new_item = input()
      add(new_item)
    
    if user_input == '2':
      print("Type in a item to remove from the list: ")
      remove_item = input()
      delete(remove_item)

    if user_input == '3':
      print("See the list of items below: ")
      list()

    #print(user_input)
if __name__ == '__main__':
  main()