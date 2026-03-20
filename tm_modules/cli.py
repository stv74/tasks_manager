"""
Module cli.py
Contains the main loop of the Console Task Manager (CTM) application, which handles user input and dispatches commands to the appropriate functions in the core module. The CLI provides an interface for users to interact with their tasks and lists, allowing them to create, view, edit, complete, and delete tasks and lists through simple text commands.
"""

from datetime import datetime
from .core import add_list, add_task, list_tasks, edit_task, remove_task, complete_task
from .config import VERSION
import shlex

def main_loop(tm_data):
    """
    Main function of the program, which handles user input and dispatches commands to the appropriate functions in the core module.
    """
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
        "delete": remove
    }

    # Main loop
    while True:
        user_input = input("Enter the command: ").strip()            
        if not user_input:
            continue
        parts = shlex.split(user_input)
        command = parts[0].lower()
        arguments = parts[1:]
        if command in commands:
            command_func = commands[command]
            command_func(tm_data, arguments) 
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
def add(tm_data, arguments):
    """
    Handles the 'add' command, allowing users to create new tasks or lists. If the user does not specify whether they want to add a task or a list, the function will prompt them to choose. It then collects the necessary information for the chosen type (title, description, priority, list ID) and calls the appropriate function from the core module to create the task or list.
    """
    # Specify what needs to be created (list or task), if not specified
    if not arguments:
        input_type = input("Choose what to create - a task or a list? ").strip().lower()
        if input_type == 'task' or input_type == 'list':
            arguments.append(input_type)
        else:
            print("Invalid choice. Task cannot be created.")
            return
        
    # Dictionary for storing input results
    user_input_map = {}

    # Getting common inputs
    while True:
        title = input("Enter a title: ").strip()
        if title:
            user_input_map['title'] = title
            break
    user_input_map['description'] = input("Enter a description (optional): ").strip()    
    if arguments[0] == 'list':
        # Getting list-specific inputs
        list_id = add_list(tm_data, user_input_map)
        print(f"List with ID {list_id} added successfully.")
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
        add_task(tm_data, user_input_map)
        print("Task added successfully.")
# End of add function

def remove(tm_data, arguments):
    """
    Handles the "delete" command, which allows users to delete tasks or lists.
    """
    if not arguments:
        input_id = input("Enter the number of the list or task you want to delete.").strip()
        arguments.append(input_id)
    
    
    

def send_message(message):
    """
    Displays informational messages to the user that do not require any action from him.
    """
    print(message)