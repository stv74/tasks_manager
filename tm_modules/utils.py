"""
Module utils.py
Contains only technical tools that do not depend on other modules.
"""

import re

TASK_PREFIX = 'T-'
LIST_PREFIX = 'L-'
ID_PATTERN = rf"^{TASK_PREFIX}(\d+)$"

def parse_id_to_int(id_str):
    """Extracts a numeric value from an ID of type 'T-102'. Returns None if the format is invalid.
    
    param id_str: The ID string to be parsed, expected to be in the format 'T-<number>'.
    """
    if not isinstance(id_str, str):
        return None
    match = re.match(ID_PATTERN, id_str)
    return int(match.group(1)) if match else None

def format_int_to_id(id_num):
    """
    Converts a number to a string in 'T-102' format.

    param id_num: The number to be converted.
    return: A string in the format 'T-<number>'.
    """
    return f"{TASK_PREFIX}{id_num}"