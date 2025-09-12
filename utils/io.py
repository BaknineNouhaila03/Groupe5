from task import Task
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

SPLIT = ";"
LOG_FILE = "logs.txt"

def read_tasks(path):
    tasklist: dict[int, Task] = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                task_id, description, state, started_at, recurrence = line.split(SPLIT)
                recurrence_parts = recurrence.split("|")
                recurrence_type = recurrence_parts[0]
                tasklist[int(task_id)] = Task(
                    task_id,
                    description,
                    state,
                    datetime.strptime(started_at, "%Y/%m/%d %H:%M:%S"),
                    recurrence_type,
                )
    return tasklist


def add_duration(date_obj: datetime, recurrence: str) -> datetime:
    if recurrence.lower() == "weekly":
        nouvelle_date = date_obj + timedelta(weeks=1)
    elif recurrence.lower() == "monthly":
        nouvelle_date = date_obj + relativedelta(months=1)
    elif recurrence.lower() == "no":
        nouvelle_date = date_obj
    else:
        raise ValueError("recurrence invalide")
    return nouvelle_date


def write_tasks(path, tasklist: dict[int, Task]):
    try:
        with open(path, "w", encoding="utf-8") as f:
            for task in tasklist.values():
                recurrence_str = task.recurrence
                if recurrence_str:  # add next recurrence date
                    try:
                        next_date = add_duration(task.started_at, recurrence_str)
                        recurrence_str = f"{recurrence_str}|{next_date.strftime('%Y/%m/%d %H:%M:%S')}"
                    except Exception as e:
                        print(f"Error calculating next recurrence for task {task.id}: {e}")

                f.write(
                    str(task.id) + SPLIT +
                    task.description + SPLIT +
                    task.state + SPLIT +
                    datetime.strftime(task.started_at, "%Y/%m/%d %H:%M:%S") + SPLIT +
                    recurrence_str + "\n"
                )
    except Exception as e:
        print(f"Error writing to file: {e}")


def write_logs(path, action: str, result: str):
    try:
        with open(path, "a+", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            f.write(timestamp + " action:" + action + " result:" + result + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
