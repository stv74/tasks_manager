#!/usr/bin/env python3

import json
import os
from datetime import datetime

# Функції для керування завданнями
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

# Функції для роботи з файлом даних
def load_tasks(file_path):
    pass

def save_tasks(file_path, tasks):
    pass

# Головна функція програми
def main():
    file_path = 'tasks.json'
    tasks = load_tasks(file_path)

    print("--- Консольний Таск-Менеджер v1.0 ---")
    print("Для початку роботи введіть одну з наступних команд: ")
    print("add - додати завдання або список;")
    print("list - подивитися списки та завдання;")
    print("edit - редагувати завдання або список;")
    print("complete - відмітити завдання як завершене;")
    print("delete - видалити завдання або список;")
    print("help - отримати допомогу;")
    print("exit - вийти з програми.")

    while True:
        command = input("Введіть команду: ").strip()
        

if __name__ == "__main__":
    main()


