#print("Om muruga saranam Om sairam")
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list
    of To-do items.
    """
    with open(filepath, "r") as f:
        todos_local = f.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write To-do items in the text file. """
    with open(filepath,'w') as f:
        f.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())