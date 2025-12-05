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
# End of main function

def add(tasks, arguments):
    pass