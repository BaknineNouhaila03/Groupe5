from task import Task
from utils.print import print_tasks


def add(tasklist: dict[int, Task], description: str , etat: str):
    if etat not in [ "started", "suspended", "completed","cancelled"]:
            print("etat doit etre soit started, suspended, completed ou cancelled")
            return (f"[error] Status not provided as required.")
    task_id = max((tasklist.keys()), default=0) + 1
    tasklist[task_id] = Task(str(task_id), description , etat)
    print("Task added with ID:", task_id)
    return (f"[success] New task added successfully: ID {task_id}; "
            f"Description \"{description}\"; Status \"{etat}\".")


def modify(tasklist: dict[int, Task], task_id: int, description : str = None, etat: str  = None ):
    if description is None and etat is None:
        print("One of the arguments -d/--description -e/--etat is required.")
        return (f"[error] No parameters provided: description or status missing.")
    try:
        if description is not None : 
         tasklist[task_id].description = description
        if etat is not None : 
         if etat not in [ "started", "suspended", "completed","cancelled"]:
            print("etat doit etre soit started, suspended, completed ou cancelled")
            return (f"[error] Status not provided as required.")
         tasklist[task_id].etat = etat
        return (f"[success] Task  with ID {task_id} successfully modified:"
                f"description updated to \"{tasklist[task_id].description}\", "
                f"status updated to \"{tasklist[task_id].etat}\".")
    except KeyError:
        print(f"Task with ID {task_id} not found.")
        return (f"[error] Task with ID {task_id} not found.")
    

def rm(tasklist: dict[int, Task], task_id: int):
    try:
        del tasklist[task_id]
        return (f"[success] Task with ID {task_id} successfully removed.")
    except KeyError:
        print(f"[error] Task with ID {task_id} not found.")
    


def show(tasklist: dict[int, Task]):
    sorted_tasks = dict(sorted(tasklist.items()))
    print_tasks(sorted_tasks)
    return (f"[success] All tasks displayed successfully.")
