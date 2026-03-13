#!/usr/bin/env python3

import sys
from tm_modules.core import get_data, send_data
from tm_modules.cli import main_loop
from tm_modules.exceptions import TaskManagerError, StorageError, DataSaveError

if __name__ == "__main__":
    try:
        get_data()
    except FileNotFoundError:
        print("Data file not found. Creating a new empty one")
    except StorageError as e:
        print(f"Unable to read data. {e}")
        sys.exit(1)

    try:
        main_loop()
    except EOFError:
        print("\nExiting program. Goodbye!")
    except TaskManagerError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            send_data()
        except DataSaveError as e:
            print(f"Unable to save data. {e}")
        else:
            print("Data saved. Exiting program. Goodbye!")


