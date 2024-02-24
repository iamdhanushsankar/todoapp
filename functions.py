FILEPATH ="task.txt"

def get_todos(filepath=FILEPATH):
    # Open file in read mod
    with open(filepath, 'r') as file_local:
             # Read all lines from file
            todos_local = file_local.readlines()
    # Return list of todos
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
      """Write todos to file.
    todos_arg: List of strings representing todos.
    filepath: File path where todos will be written.
    """    
      with open(filepath, 'w') as file:
            # Write todos to file
            file.writelines(todos_arg)


if __name__ == "__todo.py__":
      print("iam here")
      print(get_todos())           
