"""
Module storage.py 
Contains functions for storing and retrieving data in the Task Manager application.
"""

import json
import os
from .config import DATA_FILE
from .exceptions import InvalidDataFormat, DataLoadError, DataSaveError

def load_data():
    """
    Loads data from a JSON file.
    """
    try:        
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file) 
    
    except json.JSONDecodeError as e:
        raise InvalidDataFormat(f"JSON decoding error: {e}") from e
    
    except OSError as e:
        raise DataLoadError(f"File read error: {e}") from e

def save_data(tm_data):
    """
    Saves data back to a JSON file using atomic write.
    """
    temp_file = DATA_FILE + '.tmp'
    try:
        with open(temp_file, 'w', encoding='utf-8') as file:
            json.dump(tm_data, file, indent=4, ensure_ascii=False)
        os.replace(temp_file, DATA_FILE)
    except OSError as e:
        raise DataSaveError(f"File write error: {e}") from e