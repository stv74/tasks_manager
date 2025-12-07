from datetime import datetime
from .core import add, add_list, add_task, list_tasks, edit_task, remove_task, complete_task
from .storage import load_tasks, save_tasks
from .config import DATA_FILE, VERSION
import shlex

# Main function of the program
def main_loop(tasks):
    print(f"--- Console Task Manager v{VERSION} ---")
    print("To get started, enter one of the following commands: ")
    print("add - add a task or list;")
    print("list - view lists and tasks;")
    print("edit - edit a task or list;")
    print("complete - mark task as completed;")
    print("delete - delete a task or list;")
    print("help - get help;")
    print("exit - exit the program.")

    # Command Dispatcher
    commands = {
        "add": add,
        "list": list_tasks,
        "edit": edit_task,
        "complete": complete_task,
        "delete": remove_task
    }

    # Main loop
    while True:
        try:
            user_input = input("Enter the command: ").strip()
        except EOFError:
            print("\nExiting program. Goodbye!")
            break
        if not user_input:
            continue
        parts = shlex.split(user_input)
        command = parts[0].lower()
        arguments = parts[1:]
        if command in commands:
            command_func = commands[command]
            command_func(tasks, arguments) 
        elif command == "help":
            print("Available commands:")
            for cmd in commands.keys():
                print(f"- {cmd}")
        elif command == "exit":
            break
        else:
            print(f"Unknown command {command}. Type 'help' for assistance.")
# End of main_loop function

# Creating lists and tasks
def add(tasks, arguments):
    # Specify what needs to be created (list or task), if not specified
    if not arguments:
        input_type = input("Choose what to create - a task or a list? ").strip().lower()
        if input_type == 'task' or input_type == 'list':
            arguments.append(input_type)
        else:
            print("Invalid choice.")
            return
        
    # Dictionary for storing input results
    user_input_map = {}

    # Getting common inputs
    while True:
        title = input("Enter a title: ").strip()
        if title:
            user_input_map['title'] = title
            break
    description = input("Enter a description (optional): ").strip()
    if description:
        user_input_map['description'] = description
    if arguments[0] == 'list':
        list_id = add_list(tasks, user_input_map)
        print(f"List width ID {list_id} added successfully.")
    elif arguments[0] == 'task':
        # Getting task-specific inputs
        priority = input("Enter priority (low, medium, high) [default: medium]: ").strip().lower()
        if priority in ['low', 'medium', 'high']:
            user_input_map['priority'] = priority
        else:
            user_input_map['priority'] = 'medium'
        input_list_id = input("Enter the list ID to add the task to (leave blank for no list): ").strip()
        if input_list_id:
            user_input_map['list_id'] = input_list_id
        add_task(tasks, user_input_map)
        print("Task added successfully.")
# End of add function