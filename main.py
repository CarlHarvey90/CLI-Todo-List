import sys

def menu():
  menu = ("Select one of the following options by entering the option number: \n"
    "1. Add an item \n"
    "2. Remove an item \n"
    "3. View item list \n"
    "4. Exit \n")
  print(menu)

def add(add_item):
  print("New item added: " + add_item)
  menu()

def delete(delete_item):
  print("Item deleted: " + delete_item)  
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
      remove_item = input()
      delete(remove_item)

    #print(user_input)
if __name__ == '__main__':
  main()