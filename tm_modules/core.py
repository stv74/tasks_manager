"""
Module core.py
Contains the main logic for managing tasks, including functions for adding, editing, deleting, and displaying tasks.
"""

from .storage import load_data, save_data
from .models import Task, TaskList
from . import exceptions
from datetime import datetime

# Global variables to hold tasks and task lists in memory
tasks = []
task_lists = []

# Reading/storage and primary data processing
def get_data():
    """
    Receives, validates, and transforms data from the storage file.     
    """
    tm_data = load_data()
    global tasks, task_lists
    if isinstance(tm_data, dict) and 'tasks' in tm_data and 'taskLists' in tm_data and isinstance(tm_data['tasks'], list) and isinstance(tm_data['taskLists'], list):
        for task in tm_data['tasks']:
            if isinstance(task, dict):
                tasks.append(Task.from_dict(task))
        for task_list in tm_data['taskLists']:
            if isinstance(task_list, dict):
                task_lists.append(TaskList.from_dict(task_list))
    else:
        raise exceptions.InvalidDataFormat("The structure of the data file is incorrect.")      

def send_data():
    """
    Transforms data before saving to the storage file.
    """
    tm_data = {
        'tasks': [task.to_dict() for task in tasks],
        'taskLists': [task_list.to_dict() for task_list in task_lists]
    }
    save_data(tm_data)

# Функції для керування завданнями
def add(tasks, task):
    pass

def add_list(tasks, task_list):
    pass

def add_task(tasks, task):
    pass

def list_tasks(tasks):
    pass

def edit_task(tasks, task_id, new_task):
    pass

def remove_task(tasks, task_id):
    pass

def complete_task(tasks, task_id):
    pass