# Working with a data file
import json
from .exceptions import InvalidDataFormat, DataLoadError, DataSaveError

def load_data(file_path):
    try:        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)            

    except FileNotFoundError:
        return {"tasks": [], "taskLists": []}
    
    except json.JSONDecodeError as e:
        raise InvalidDataFormat(f"JSON decoding error: {e}") from e
    
    except (IOError, OSError) as e:
        raise DataLoadError(f"File read error: {e}") from e

    return data

def save_data(file_path, tm_data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(tm_data, file, indent=4, ensure_ascii=False)

    except (IOError, OSError) as e:
        raise DataSaveError(f"File write error: {e}") from e
    
    except TypeError as e:
        raise DataSaveError(f"Data serialization error: {e}") from e
    
    return True