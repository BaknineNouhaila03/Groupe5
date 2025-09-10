from utils import parser, io
from commands import add, rm, modify, show


def main():
    args = parser.parse_args()

    try:
        tasklist = io.read_tasks(args.path)
        match args.command:
            case "add":
                add(tasklist, args.description)
            case "modify":
                modify(tasklist, args.task_id, args.description)
            case "rm":
                rm(tasklist, args.task_id)
            case "show":
                show(tasklist)

        io.write_tasks(args.path, tasklist)

    except FileNotFoundError:
        print("Task file not found.")
        return False


if __name__ == "__main__":
    main()
