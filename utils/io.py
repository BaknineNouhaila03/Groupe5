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
                task_id, description, etat = line.strip().split(SPLIT)
                tasklist[int(task_id)] = Task(task_id, description, etat)
    return tasklist


def write_tasks(path, tasklist: dict[int, Task]):
    try:
        with open(path, "w", encoding="utf-8") as f:
            for task in tasklist.values():
                f.write(str(task.id) + SPLIT + task.description + SPLIT +
                        task.etat + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

def write_logs(path, action: str, result: str):
    try:
        with open(path, "w", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            f.write(timestamp + "\taction:" + action + "\tresult:" + result +
                    "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

