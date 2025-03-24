import sys

def add():
  print("I am add")

def main():
  
  while True:
    user_input = input("Please enter something: ")
  
    if user_input.lower() == "exit":
      print("Exiting Todo List")
      break
    
    if user_input == 'add':
      add()

    print(user_input)
if __name__ == '__main__':
  main()