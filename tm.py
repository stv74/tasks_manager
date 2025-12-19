#!/usr/bin/env python3

from tm_modules.storage import load_data, save_data
from tm_modules.cli import main_loop
from tm_modules.config import DATA_FILE

if __name__ == "__main__":
    tm_data = load_data(DATA_FILE)
    main_loop(tm_data)
    save_data(DATA_FILE, tm_data)
    print("Data saved. Exiting program. Goodbye!")


