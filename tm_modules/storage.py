"""
Module storage.py 
Contains functions for storing, retrieving and validating data in the Task Manager application.
"""

import os
import json
import shutil
from .utils import parse_id_to_int, format_int_to_id
from .exceptions import InvalidDataFormat, DataLoadError, DataSaveError

def load_data(path):
    """
    Loads data from a JSON file and validates it.
    """
    try:        
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Data validation
            cleaned_data, message = validate_data(data)

            # If there are error messages, make a backup of the original file before returning the cleaned data.
            if message:
                if _create_backup(path):
                    message += f"\nBackup saved in: {path}.bak"
                else:
                    message += "\nWarning: Failed to create backup file!" 

            return cleaned_data, message
    
    except json.JSONDecodeError as e:
        raise InvalidDataFormat(f"JSON decoding error: {e}") from e    
    except OSError as e:
        raise DataLoadError(f"File read error: {e}") from e

def save_data(tm_data, path):
    """
    Saves data back to a JSON file using atomic write.
    """
    temp_file = path + '.tmp'
    try:
        with open(temp_file, 'w', encoding='utf-8') as file:
            json.dump(tm_data, file, indent=4, ensure_ascii=False)
        os.replace(temp_file, path)
    except OSError as e:
        raise DataSaveError(f"File write error: {e}") from e

def _create_backup(path):
    """
    Creates a copy of a file with the extension .bak

    param path: The path of the file to be backed up.
    return: True if the backup was created successfully, False otherwise.
    """
    try:
        backup_path = path + ".bak"
        shutil.copy2(path, backup_path) 
        return True
    except OSError:
        return False

def _is_item_valid(item, schema):
        """
        Technical check: Does the dictionary conform to the given type scheme?

        param item: The dictionary to be validated.
        param schema: A dictionary defining the required fields and their expected types.
        return: True if the item is valid according to the schema, False otherwise.
        """
        if not isinstance(item, dict): return False
        # Basic validation of required fields and their types
        for field, expected_type in schema.items():
            if field not in item or not isinstance(item[field], expected_type):
                return False
        return True

def validate_data(data):
    """
    Validates the structure and content of the loaded data. It checks for the presence of required sections ('tasks' and 'taskLists') and validates each task and list against predefined schemas. If any tasks or lists are found to be corrupted (missing required fields or having incorrect types), they are removed from the data, and a warning message is generated indicating how many items were deleted. The function returns the cleaned data along with any warning messages.

    param data: The raw data loaded from the JSON file, expected to be a dictionary containing 'tasks' and 'taskLists'.
    return: A tuple containing the cleaned data and an optional warning message about any corrupted items that were removed.
    """
    # Basic check for the presence of main sections
    if not isinstance(data, dict) or 'tasks' not in data or 'taskLists' not in data:
        raise InvalidDataFormat("The file is missing 'tasks' or 'taskLists' sections'.")

    # Validation schemas
    task_fields = {"id": str, "title": str, "description": str, "status": str, "priority": str, "completed": bool, "is_part_of_list": bool} 
    list_fields = {"id": str, "title": str, "description": str, "tasks": list}    

    # Cleaning tasks
    original_tasks_count = len(data['tasks'])
    data['tasks'] = [t for t in data['tasks'] if _is_item_valid(t, task_fields)]
    corrupted_tasks = original_tasks_count - len(data['tasks'])

    # Cleaning lists
    original_lists_count = len(data['taskLists'])
    data['taskLists'] = [l for l in data['taskLists'] if _is_item_valid(l, list_fields)]
    corrupted_lists = original_lists_count - len(data['taskLists'])

    # Feedback generation
    message = None
    if corrupted_tasks > 0 or corrupted_lists > 0:
        message = f"Warning: {corrupted_tasks} tasks and {corrupted_lists} lists have been deleted due to errors."

    return data, message
                            

                

            
            
        