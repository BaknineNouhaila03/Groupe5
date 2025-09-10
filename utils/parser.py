import argparse
from commands import add, modify, rm, show


def parse_args():
    parser = argparse.ArgumentParser(description="Simple task manager")

    parser.add_argument(
        "path",
        type=str,
        help="Path to the task file",
        default="lestaches.txt"
    )

    subparsers = parser.add_subparsers(dest="command", required=True,
                                       help="add, modify, rm, show")
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str,
                            help="Description of the task")
    add_parser.add_argument("Etat", type=str,
                               help="New state of the task : started, suspended, cancelled and completed")
    modify_parser = subparsers.add_parser("modify",
                                          help="Modify an existing task")
    
    modify_parser.add_argument("task_id", type=int, help="ID of the task to "
                                                         "modify")
    modify_parser.add_argument("description", type=str,
                               help="New description of the task")
    modify_parser.add_argument("Etat", type=str,
                               help="New state of the task : started, suspended, cancelled and completed")
    rm_parser = subparsers.add_parser("rm", help="Remove a task")
    rm_parser.add_argument("task_id", type=int, help="ID of the task to remove"
                           )

    show_parser = subparsers.add_parser("show", help="Show all tasks")

    return parser.parse_args()
