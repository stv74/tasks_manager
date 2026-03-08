"""
Module core.py
Contains the main logic for managing tasks, including functions for adding, editing, deleting, and displaying tasks.
"""

from datetime import datetime
from tm_modules.config import DATA_FILE
from tm_modules.storage import load_data, save_data

tasks = []
task_lists = []

def get_data():
    """
    Receives, validates, and transforms data from the storage file.     
    """
    try:
        tm_data = load_data(DATA_FILE)
    except Exception as e:
        print(f"Error occurred while loading data: {e}")
        return {"tasks": [], "taskLists": []}

def send_data(tm_data):
    """
    Validates and transforms data before saving to the storage file.
    """
    try:
        save_data(DATA_FILE, tm_data)
    except Exception as e:
        print(f"Error occurred while saving data: {e}")

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