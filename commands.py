from task import Task
from utils.print import print_tasks


def add(tasklist: dict[int, Task], description: str):
    task_id = max((tasklist.keys()), default=0) + 1
    tasklist[task_id] = Task(str(task_id), description)
    print("Task added with ID:", task_id)


def modify(tasklist: dict[int, Task], task_id: int, description: str):
    try:
        tasklist[task_id].description = description
    except KeyError:
        print(f"Task with ID {task_id} not found.")


def rm(tasklist: dict[int, Task], task_id: int):
    try:
        del tasklist[task_id]
    except KeyError:
        print(f"Task with ID {task_id} not found.")


def show(tasklist: dict[int, Task]):
    sorted_tasks = dict(sorted(tasklist.items()))
    print_tasks(sorted_tasks)
