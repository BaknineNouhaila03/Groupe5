from task import Task


def print_tasks(tasklist: dict[int, Task]):
    if not tasklist:
        print("No tasks to show.")
        return
    id_width = max(len("id"), max((len(t.id) for t in tasklist.values())))
    desc_width = max(len("description"),
                     max((len(t.description) for t in tasklist.values())))
    etat_width = max(len("etat"),max((len(t.etat) for t in tasklist.values())))


    def print_grid_line():
        print(f"+{'-' * (id_width + 2)}+{'-' * (desc_width + 2)}+{'-' * (etat_width + 2)}")

    print_grid_line()
    print(f"| {'id'.ljust(id_width)} | {'description'.ljust(desc_width)} | {'etat'.ljust(etat_width)} |")
    print_grid_line()

    for task in tasklist.values():
        print(
            f"| {task.id.ljust(id_width)} | "
            f"{task.description.ljust(desc_width)} | {task.etat.ljust(etat_width)} |")

    print_grid_line()
