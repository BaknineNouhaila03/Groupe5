from task import Task
from utils.print import print_tasks


def add(tasklist: dict[int, Task], description: str , etat: str):
    if etat not in [ "started", "suspended", "completed","cancelled"]:
            print("etat doit etre soit started, suspended, completed ou cancelled")
            return (f"etat doit etre soit started, suspended, completed ou cancelled")
    task_id = max((tasklist.keys()), default=0) + 1
    tasklist[task_id] = Task(str(task_id), description , etat)
    print("Task added with ID:", task_id)
    return (f"Task added with ID: {task_id}; Description: {description}; Etat:"
            f" {etat}")


def modify(tasklist: dict[int, Task], task_id: int, description : str = None, etat: str  = None ):
    if description is None and etat is None:
        print("One of the arguments -d/--description -e/--etat is required.")
        return (f"One of the arguments -d/--description -e/--etat is required.")
    try:
        if description is not None : 
         tasklist[task_id].description = description
        if etat is not None : 
         if etat not in [ "started", "suspended", "completed","cancelled"]:
            print("etat doit etre soit started, suspended, completed ou cancelled")
            return (f"etat doit etre soit started, suspended, completed ou cancelled")
         tasklist[task_id].etat = etat
        return (f"Task  with ID: {task_id} modified ; Result :  Description: {tasklist[task_id].description}; Etat:"
            f" {tasklist[task_id].etat}")
    except KeyError:
        print(f"Task with ID {task_id} not found.")
        return (f"Task with ID {task_id} not found.")
    

def rm(tasklist: dict[int, Task], task_id: int):
    try:
        del tasklist[task_id]
        return (f"Task  with ID: {task_id} removed;")
    except KeyError:
        print(f"Task with ID {task_id} not found.")
    


def show(tasklist: dict[int, Task]):
    sorted_tasks = dict(sorted(tasklist.items()))
    print_tasks(sorted_tasks)
    return (f"Tasks showed")
