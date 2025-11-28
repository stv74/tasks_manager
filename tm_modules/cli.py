from datetime import datetime
from .core import add, add_list, add_task, list_tasks, edit_task, remove_task, complete_task
from .storage import load_tasks, save_tasks
from .config import DATA_FILE, VERSION

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

    while True:
        command = input("Enter the command: ").strip().lower().split()
        command_length = len(command)
        if command_length == 0:
            continue     
        if command[0] == "add":
            if command[1] == "-l":
                add_list(tasks)
            elif command[1] == "-t":
                add_task(tasks)
            else: 
                add(tasks)
        elif command_length <= 4 and command == "list":
            pass  # Логіка виведення списку завдань
        elif command_length <= 4 and command[0] == "edit":
            pass  # Логіка редагування завдання
        elif command_length <= 2 and command[0] == "complete":
            pass  # Логіка відмітки завдання як завершеного
        elif command_length <= 2 and command[0] == "delete":
            pass  # Логіка видалення завдання
        elif command_length <= 2 and command[0] == "help":
            print("Доступні команди: add, list, edit, complete, delete, help, exit")
        elif command_length == 1 and command[0] == "exit":
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Unknown command. Type 'help' for assistance.")