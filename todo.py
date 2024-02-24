import functions
import time

now = time.strftime(["%b %d, %Y %H:%M:%S"])
print(f"{now} Starting the program...\n")


while True:
    user = input("Type Add, Show, edit, complete, or Exit: ")
    user = user.strip() 

    
    if user.startswith("add"):
        todo = user[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

        
    elif user.startswith("show"):
        
        todos = functions.get_todos()
            
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}:{item}"
            print(row)

    elif user.startswith('edit'):
        try:
            number = int(user[5:])
            print(number)

            number = number - 1 

            todos = functions.get_todos()  

            new_todo = input("enter the new task: ")
            todos[number] = new_todo + '\n'
            
            functions.write_todos(todos)
        except ValueError:
            print("Your command is invaild:( ") 
            continue   

    elif user.startswith('complete'):
        try:
            number = int(user[9:])

            todos = functions.get_todos()
            index = number - 1
            todotoremove = todos[index].strip('\n')
            todos.pop(index)   

            functions.write_todos(todos)

            message = f"Task {todotoremove} was removed from your task."
            print(message)
        except IndexError:
            print("there is no item in that number.")
            continue                 

    elif user.startswith('exit'):
        break

    else:
        print("the command is invaild you bastard :( ")

print("bye!") 

