from task import Task
from datetime import datetime

SPLIT = ";"
LOG_FILE = "logs.txt"

def read_tasks(path):
    tasklist: dict[int, Task] = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                task_id, description, state, started_at, recurrence = line.strip(

                ).split(SPLIT)
                tasklist[int(task_id)] = Task(task_id, description, state,
                                              datetime.strptime(started_at,"%Y/%m/%d %H:%M:%S"),
                                              recurrence)
    return tasklist


def write_tasks(path, tasklist: dict[int, Task]):
    try:
        with open(path, "w", encoding="utf-8") as f:
            for task in tasklist.values():
                f.write(str(task.id) + SPLIT + task.description + SPLIT +
                        task.state + SPLIT + datetime.strftime(
                    task.started_at,"%Y/%m/%d %H:%M:%S") + SPLIT +
                        task.recurrence + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

def write_logs(path, action: str, result: str):
    try:
        with open(path, "a+", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            f.write(timestamp + " action:" + action + " result:" + result +
                    "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

