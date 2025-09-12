from task import Task


def print_tasks(tasklist: dict[int, Task]):
    if not tasklist:
        print("No tasks to show.")
        return
    id_width = max(len("id"), max((len(t.id) for t in tasklist.values())))
    desc_width = max(len("description"),
                     max((len(t.description) for t in tasklist.values())))
    state_width = max(len("state"),max((len(t.state) for t in tasklist.values())))
    recurrence_width = max(len("recurrence"),max((len(t.state) for t in tasklist.values())))



    def print_grid_line():
        print(f"+{'-' * (id_width + 2)}+{'-' * (desc_width + 2)}+"
              f"{'-' * (state_width + 2)}+{'-' * (recurrence_width + 2)}")

    print_grid_line()
    print(f"| {'id'.ljust(id_width)} | {'description'.ljust(desc_width)} | {'state'.ljust(state_width)} | {'recurrence'.ljust(recurrence_width)} |")
    print_grid_line()

    for task in tasklist.values():
        print(
            f"| {task.id.ljust(id_width)} | "
            f"{task.description.ljust(desc_width)} | {task.state.ljust(state_width)} | {task.recurrence.ljust(recurrence_width)} |")

    print_grid_line()
