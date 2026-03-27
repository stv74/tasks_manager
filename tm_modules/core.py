"""
Module core.py
Contains the main logic for managing tasks, including functions for adding, editing, deleting, and displaying tasks.
"""

from .storage import load_data, save_data
from .models import Task, TaskList
from . import exceptions
from datetime import datetime

# Reading/storage and primary data processing
def get_data(path):
    """
    Receives, validates, and transforms data from the storage file.     
    """
    tm_data = {"tasks": [], "taskLists": []}
    data_file = load_data(path)
    if isinstance(data_file, dict) and 'tasks' in data_file and 'taskLists' in data_file and isinstance(data_file['tasks'], list) and isinstance(data_file['taskLists'], list):
        for task in data_file['tasks']:
            if isinstance(task, dict):
                tm_data['tasks'].append(Task.from_dict(task))
        for task_list in data_file['taskLists']:
            if isinstance(task_list, dict):
                tm_data['taskLists'].append(TaskList.from_dict(task_list))
    else:
        raise exceptions.InvalidDataFormat("The structure of the data file is incorrect.")      

def send_data(tm_data, path):
    """
    Transforms data before saving to the storage file.
    """
    data_file = {
        'tasks': [task.to_dict() for task in tm_data['tasks']],
        'taskLists': [task_list.to_dict() for task_list in tm_data['taskLists']]
    }
    save_data(data_file, path)

# The function for management of tasks and lists.
def add_list(tm_data, user_input_map):
    """
    Handles the creation of a new task list. It takes a dictionary containing the title and optional description of the list, creates a new TaskList object, and adds it to the global task_lists variable. The function returns the ID of the newly created list.

    :param user_input_map: A dictionary containing the title and optional description of the list to be created.
    :return: The ID of the newly created list.
    """
    id = generate_id(tm_data['taskLists'], 'L')
    user_input_map['id'] = id
    tm_data['taskLists'].append(TaskList.from_dict(user_input_map))
    return id

def add_task(tm_data, user_input_map):
    """
    Handles the creation of a new task. It takes a dictionary containing the task details, creates a new Task object, and adds it to the global tasks variable. The function returns the ID of the newly created task.

    :param user_input_map: A dictionary containing the details of the task to be created, including title, description, priority, and optional list ID.
    """
    id = generate_id(tm_data['tasks'], 'T')
    user_input_map['id'] = id
    tm_data['tasks'].append(Task.from_dict(user_input_map))

def generate_id(data, prefix):
    """
    Generates a unique ID for a new task or list by finding the maximum existing ID in the current data and incrementing it by one. This ensures that each new task or list has a unique identifier.

    :param data: The current data containing existing tasks and lists.
    :param prefix: A string indicating whether the ID is for a task ('T') or a list ('L').
    :return: A unique string ID for the new task or list.
    """
    if not data:
        if prefix == 'T':
            return 'T1'
        elif prefix == 'L':
            return 'L1'
    for item in data:
        
        
    #max_id = max(item.id[1:] for item in data)
    #return max_id + 1

def remove_task(tasks, task_id):
    pass

def list_tasks(tasks):
    pass

def edit_task(tasks, task_id, new_task):
    pass


def complete_task(tasks, task_id):
    pass

