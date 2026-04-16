#!/usr/bin/env python3

import sys
from tm_modules.config import DATA_FILE_PATH
from tm_modules.core import TaskManager
from tm_modules.cli import main_loop
from tm_modules.exceptions import TaskManagerError, StorageError, DataSaveError

if __name__ == "__main__":
    try:
        manager = TaskManager(DATA_FILE_PATH)
        if manager.message:
            print(manager.message)
        main_loop(manager)

    except StorageError as e:
        print(f"Critical startup error: {e}")
        sys.exit(1)

    except EOFError:
        print("\nExiting program. Goodbye!")

    except TaskManagerError as e:
        print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # We save data only if the manager was created successfully
        if 'manager' in locals():
            try:
                manager.save()
                print("Data saved. Exiting program. Goodbye!")
            except DataSaveError as e:
                print(f"Unable to save data. {e}")


