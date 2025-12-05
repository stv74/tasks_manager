#!/usr/bin/env python3

from tm_modules.storage import load_tasks, save_tasks
from tm_modules.cli import main_loop
from tm_modules.config import DATA_FILE

if __name__ == "__main__":
    tasks = load_tasks(DATA_FILE)
    main_loop(tasks)
    save_tasks(DATA_FILE, tasks)
    print("Data saved. Exiting program. Goodbye!")


