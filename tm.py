#!/usr/bin/env python3

from tm_modules.core import get_data, send_data
from tm_modules.cli import main_loop
from tm_modules.exceptions import TaskManagerError

if __name__ == "__main__":
    tm_data = get_data()
    main_loop(tm_data)
    send_data(tm_data)
    print("Data saved. Exiting program. Goodbye!")


