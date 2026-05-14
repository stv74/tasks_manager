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
        print(f"\nCritical startup error: {e}")
        sys.exit(1)

    except TaskManagerError as e:
        print(f"\nAn error occurred! {e}")

    except EOFError:
        print(f"\nProgram execution interrupted")

    except Exception as e:
        print(f"\nAn unexpected error occurred! {e}")

    finally:
        # We save data only if the manager was created successfully
        if 'manager' in locals():
            try:
                manager.save()
                print("\nData saved. Exiting program. Goodbye!")
            except DataSaveError as e:
                print(f"\nUnable to save data! {e}")


