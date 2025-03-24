import sys
menu = ("Select one of the following options: \n"
  "1. Add another item \n"
  "2. Remove an item \n"
  "3. View item list \n"
  "4. Home \n")

def add(user_input):
  print("New item added " + user_input)
  print(menu)
  #print("Select one of the following options: ")
  #print("1. Add another item")
  #print("2. Remove an item")
  #print("3. View item list")
  #print("4. Home")
  

def main():
  welcome = ("Welcome to the Todo list app. Please choose one of the following options: \n"
  "1. Add an item \n"
  "2. Remove and item \n"
  "3. View item list \n"
  "4. Exit")
  print(welcome)
  #print(menu)
  while True:
    
    user_input = input()
    
    if user_input.lower() == "exit" or "4":
      print("Exiting Todo List")
      break
    
    if user_input == '1':
      print("Type in a item to add to the list: ")
      new_item = input()
      add(new_item)

    #print(user_input)
if __name__ == '__main__':
  main()