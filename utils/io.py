from task import Task

SPLIT = "|"


def read_tasks(path):
    tasklist: dict[int, Task] = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                task_id, description = line.split("|", 1)
                tasklist[int(task_id)] = Task(task_id, description)
    return tasklist


def write_tasks(path, tasklist: dict[int, Task]):
    try:
        with open(path, "w", encoding="utf-8") as f:
            for task in tasklist.values():
                f.write(str(task.id) + SPLIT + task.description + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
