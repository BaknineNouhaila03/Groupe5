from datetime import datetime, timedelta

from matplotlib.dates import relativedelta
from task import Task
from utils.print import print_tasks


def add(tasklist: dict[int, Task], description: str , state: str , recurrence: str ):
    if state not in [ "started", "suspended", "completed","cancelled"]:
            print("State must be one of: started, suspended, completed ou cancelled")
            return (f"[error] Status not provided as required.")
    task_id = max((tasklist.keys()), default=0) + 1
    tasklist[task_id] = Task(str(task_id), description , state , datetime.now() , recurrence)
    print("Task added with ID:", task_id)
    return (f"[success] New task added successfully: ID {task_id}; "
            f"Description \"{description}\"; Status \"{state}\"; Recurrence \"{recurrence}\".")


def modify(tasklist: dict[int, Task], task_id: int, description : str = None, state: str  = None, recurrence :str = None ):
    if description is None and state is None and recurrence is None:
        print("One of the arguments -d/--description -e/--state -r/--recurrence is required.")
        return (f"[error] No parameters provided: description , status or recurrence missing.")
    try:
        if description is not None : 
         tasklist[task_id].description = description
        if state is not None : 
         if state not in [ "started", "suspended", "completed","cancelled"]:
            print("State must be one of: started, suspended, completed ou cancelled")
            return (f"[error] Status not provided as required.")
         tasklist[task_id].state = state
        if recurrence is not None :
         if recurrence not in [ "weekly", "monthly", "No recurrence"]:
            print("recurrence must be one of: weekly , monthly , No recurrence")
            return (f"[error] Status not provided as required.")            
        return (f"[success] Task  with ID {task_id} successfully modified:"
                f"description updated to \"{tasklist[task_id].description}\", "
                f"status updated to \"{tasklist[task_id].state}\",")
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

def add_duration(date_obj: datetime, recurrence: str) -> datetime:

    if recurrence.lower() == "weekly":
        nouvelle_date = date_obj + timedelta(weeks=1)
    elif recurrence.lower() == "monthly":
        nouvelle_date = date_obj + relativedelta(months=1)
    else:
        raise ValueError("recurrence invalide")
    
    return nouvelle_date

