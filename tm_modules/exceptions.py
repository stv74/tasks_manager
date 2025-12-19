# Exception classes
class TaskManagerError(Exception):
    """Base exception class for Task Manager errors."""
    pass

class StorageError(TaskManagerError):
    """Basic exception for errors related to data storage."""
    pass

class DataLoadError(StorageError):
    """Occurs when data cannot be loaded (problems with the file or JSON)."""
    pass

class InvalidDataFormat(StorageError):
    """Occurs when a JSON file is uploaded but its structure is invalid."""
    pass

class DataSaveError(StorageError):
    """Occurs when it is impossible to record data."""
    pass


class CoreError(TaskManagerError):
    """Basic exception for errors in core functionalities."""
    pass

class TaskNotFoundError(CoreError):
    """Occurs when a task with the specified ID is not found."""
    pass

class ListNotFoundError(CoreError):
    """Occurs when a list with the specified ID is not found."""
    pass

class TaskValidationError(CoreError):
    """Occurs when task data is invalid (e.g., empty title)."""
    pass