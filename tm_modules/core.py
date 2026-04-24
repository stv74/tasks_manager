"""
Module core.py
Contains the TaskManager class which provides methods for managing tasks and task lists. 
"""

from .storage import load_data, save_data
from .models import Task, TaskList
from . import exceptions
from datetime import datetime

class TaskManager:
    """
    A class that manages tasks and task lists, providing methods for adding, editing, deleting, and displaying tasks. It interacts with the storage module to load and save data, and uses the Task and TaskList classes from the models module to represent individual tasks and collections of tasks.
    """
    def __init__(self, path):
        self.path = path
        try:
            row_data, self.message = load_data(self.path)
        except FileNotFoundError:
            self.message = "Data file not found. Creating a new empty one"
            row_data = {"tasks": [], "taskLists": []}

        self.tasks = [Task.from_dict(task) for task in row_data['tasks']]
        self.task_lists = [TaskList.from_dict(task_list) for task_list in row_data['taskLists']]

    def save(self):
        """
        Saves the current state of tasks and task lists back to the storage file.
        """
        tm_data = {
            'tasks': [task.to_dict() for task in self.tasks],
            'taskLists': [task_list.to_dict() for task_list in self.task_lists]
        }
        save_data(tm_data, self.path)

    def add_list(self, user_input_map):
        """
        Handles the creation of a new task list. It takes a dictionary containing the title and optional description of the list, creates a new TaskList object, and adds it to the global task_lists variable. The function returns the ID of the newly created list.

        :param user_input_map: A dictionary containing the title and optional description of the list to be created.
        :return: The ID of the newly created list.
        """
        id = self._generate_id('L-')
        user_input_map['id'] = id
        task_list = TaskList.from_dict(user_input_map)
        self.task_lists.append(task_list)
        return id

    def add_task(self, user_input_map):
        """
        Handles the creation of a new task. It takes a dictionary containing the title, description, priority, and optional list ID for the task, creates a new Task object, and adds it to the global tasks variable. If a list ID is provided, the function also adds the task to the corresponding task list. The function returns the ID of the newly created task.

        :param user_input_map: A dictionary containing the title, description, priority, and optional list ID for the task to be created.
        :return: The ID of the newly created task.
        """
        if 'list_id' in user_input_map:
            list_id = user_input_map['list_id']
            for task_list in self.task_lists:
                if task_list.id == list_id:
                    task_list.list_tasks_ids.append(task.id)
                    break
            else:
                raise exceptions.ListNotFoundError(f"No list with ID {list_id} exists.")
            
        id = self._generate_id('T-')
        user_input_map['id'] = id
        user_input_map['is_part_of_list'] = 'list_id' in user_input_map
            
        task = Task.from_dict(user_input_map)
        self.tasks.append(task)
        return id
    
    def _generate_id(self, prefix):
        """
        Generates a unique ID for a new task or list by finding the maximum existing ID in the current data and incrementing it by one. This ensures that each new task or list has a unique identifier.

        :param prefix: A string indicating whether the ID is for a task ('T-') or a list ('L-').
        :return: A unique string ID for the new task or list.
        """
        if prefix == 'T-':
            data = self.tasks
        elif prefix == 'L-':
            data = self.task_lists
        else:
            raise ValueError("Invalid prefix. Use 'T-' for tasks and 'L-' for lists.")
        
        if not data:
            return f"{prefix}1"
        
        max_id = max((int(i.id[2:])) for i in data)
        return f"{prefix}{max_id + 1}"
   



# The function for management of tasks and lists.






def remove_task(tasks, task_id):
    pass

def list_tasks(tasks):
    pass

def edit_task(tasks, task_id, new_task):
    pass


def complete_task(tasks, task_id):
    pass

