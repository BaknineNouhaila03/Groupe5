from task import Task


from task import Task
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def add_duration(date_obj: datetime, recurrence: str) -> datetime:
    if recurrence.lower() == "weekly":
        return date_obj + timedelta(weeks=1)
    elif recurrence.lower() == "monthly":
        return date_obj + relativedelta(months=1)
    else:
        raise ValueError("recurrence invalide")


def print_tasks(tasklist: dict[int, Task]):
    if not tasklist:
        print("No tasks to show.")
        return

    recurrence_strings = {}
    for t in tasklist.values():
        try:
            next_date = add_duration(t.started_at, t.recurrence)
            recurrence_strings[t.id] = f"{t.recurrence} -> {next_date.strftime('%Y/%m/%d %H:%M:%S')}"
        except Exception:
            recurrence_strings[t.id] = t.recurrence  

    id_width = max(len("id"), max((len(str(t.id)) for t in tasklist.values())))
    desc_width = max(len("description"), max((len(t.description) for t in tasklist.values())))
    state_width = max(len("state"), max((len(t.state) for t in tasklist.values())))
    recurrence_width = max(len("recurrence"), max((len(r) for r in recurrence_strings.values())))

    def print_grid_line():
        print(f"+{'-' * (id_width + 2)}+{'-' * (desc_width + 2)}+"
              f"{'-' * (state_width + 2)}+{'-' * (recurrence_width + 2)}+")

    print_grid_line()
    print(f"| {'id'.ljust(id_width)} | {'description'.ljust(desc_width)} | "
          f"{'state'.ljust(state_width)} | {'recurrence'.ljust(recurrence_width)} |")
    print_grid_line()

    for t in tasklist.values():
        recurrence_str = recurrence_strings[t.id]
        print(
            f"| {str(t.id).ljust(id_width)} | "
            f"{t.description.ljust(desc_width)} | "
            f"{t.state.ljust(state_width)} | "
            f"{recurrence_str.ljust(recurrence_width)} |"
        )

    print_grid_line()

