"""
Module storage.py 
Contains functions for storing, retrieving and validating data in the Task Manager application.
"""

import json
import os
from .exceptions import InvalidDataFormat, DataLoadError, DataSaveError

def load_data(path):
    """
    Loads data from a JSON file and validates it.
    """
    try:        
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            validate_data(data)
            return data
    
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
    
def validate_data(data):
    """
    Validates the structure of the loaded data to ensure it contains the expected keys and types. This function checks that the data is a dictionary with 'tasks' and 'taskLists' keys, and that both of these keys contain lists. If the data does not meet these criteria, an InvalidDataFormat exception is raised.
    """
    # Structure check
    if not isinstance(data, dict) or 'tasks' not in data or 'taskLists' not in data or not isinstance(data['tasks'], list) or not isinstance(data['taskLists'], list) or len(data) != 2:
        raise InvalidDataFormat("The structure of the data file is incorrect.")
    
    valid_tasks = []
    valid_lists = []
    corrupted_tasks = 0
    corrupted_lists = 0
    type_map = {"id": str, "title": str, "description": str, "status": str, "priority": str, "deadline": str, "completed": bool, "is_part_of_list": bool, "tasks": list}
    
    for key in data:
        for item in data[key]:
            if not isinstance(item, dict):
                raise InvalidDataFormat("Each task/list should be a dictionary.")            
            for item_key in item:
                if item_key in type_map and isinstance(item[item_key], type_map[item_key]):
                    continue

                

            
            
        