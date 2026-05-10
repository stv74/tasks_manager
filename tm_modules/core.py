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
            self.message = "Data file not found. Creating a new empty one."
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
        id = self._generate_id('T-')
        user_input_map['id'] = id        
        task = Task.from_dict(user_input_map)
        self.tasks.append(task)           
        return id
    
    def remove(self, id):
        """
        Handles the deletion of a task or list based on the provided ID. 

        :param id: A string representing the ID of the task or list to be deleted (e.g., 'T-1' for a task or 'L-1' for a list).
        :return: A tuple containing the ID and type of the deleted item (e.g., ('T-1', 'Task') or ('L-1', 'List')).
        :raises InvalidIDError: If the provided ID format is invalid.        
        """
        if id[:2] == 'T-':
            for i, task in enumerate(self.tasks):
                if task.id == id:
                    del self.tasks[i]
                    return id, "Task"
            raise exceptions.TaskNotFoundError(f"No task with ID {id} found.")
        elif id[:2] == 'L-':
            for i, task_list in enumerate(self.task_lists):
                if task_list.id == id:
                    if next((task for task in self.tasks if task.list_id == id), None):
                        raise exceptions.ListNotFoundError(f"Cannot delete list with ID {id}. It still contains tasks.")
                    del self.task_lists[i]
                    return id, "List"
            raise exceptions.ListNotFoundError(f"No list with ID {id} found.")
        else:
            raise exceptions.InvalidIDError("Invalid ID format. Please enter a valid task ID (e.g., 'T-1') or list ID (e.g., 'L-1').")

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
            raise exceptions.InvalidIDError("Invalid prefix. Use 'T-' for tasks and 'L-' for lists.")
        
        if not data:
            return f"{prefix}1"
        
        max_id = max((int(i.id[2:])) for i in data)
        return f"{prefix}{max_id + 1}"
   
    def get_all_list_ids(self):
        """
        Retrieves a list of all existing list IDs.

        :return: A list of strings representing the IDs of all lists.
        """
        list_ids = [task_list.id for task_list in self.task_lists]
        return list_ids
