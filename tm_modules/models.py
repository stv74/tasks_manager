"""
Module models.py.
Contains the Task and TaskList classes, which are used to represent individual tasks and collections of tasks in a task management system.
"""

class Task:
    """
    A class that creates individual tasks

    Attributes
    ----------
    id : str
        Unique identifier for the task
    title : str
        Title of the task
    description : str
        Description of the task
    status : str
        Status of the task (e.g., "pending", "in progress", "completed")
    priority : str
        Priority level of the task (e.g., "low", "medium", "high")
    deadline : str
        Deadline for the task (e.g., "2024-12-31")
    completed : bool
        Indicates whether the task is completed
    list_id : str
        Identifier for the task list to which the task belongs
    """

    def __init__(self, id, title, description="", status="pending", priority="medium", deadline=None, completed=False, list_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.deadline = deadline
        self.completed = completed
        self.list_id = list_id

    def toggle(self):
        """
        Toggles the completion status of the task.
        """
        self.completed = not self.completed

    def to_dict(self):
        """
        Converts a task object into a dictionary for storage in JSON.
        """
        return vars(self)
    
    @staticmethod
    def from_dict(data):
        """
        Creates a Task object from a dictionary.
        
        :param data: Dictionary containing task data
        """
        return Task(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description", ""),
            status=data.get("status", "pending"),
            priority=data.get("priority", "medium"),
            deadline=data.get("deadline"),
            completed=data.get("completed", False),
            list_id=data.get("list_id", None)
        )
    
    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', status='{self.status}', priority='{self.priority}', deadline='{self.deadline}', completed={self.completed}, list_id={self.list_id})"

class TaskList:
    """
    A class that creates a task list, which is a collection of tasks.

    Attributes
    ----------
    id : str
        Unique identifier for the task list
    title : str
        Title of the task list
    description : str
        Description of the task list
    """
    
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description

    def to_dict(self):
        """
        Converts a task list object into a dictionary for storage in JSON.
        """
        return vars(self)
    
    @staticmethod
    def from_dict(data):
        """
        Creates a TaskList object from a dictionary.
        
        :param data: Dictionary containing task list data
        """
        return TaskList(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description", "")
        )
    
    def __str__(self):
        return f"List {self.id}: {self.title} - {self.description}"
