from utils import parser, io
from commands import add, rm, modify, show
from utils.io import LOG_FILE


def main():
    args = parser.parse_args()
    action = args.command
    result_msg = ""
    try:
        tasklist = io.read_tasks(args.path)
        match args.command:
            case "add":
                result_msg = add(tasklist, args.description, args.state)
            case "modify":
                result_msg = modify(tasklist, args.task_id, args.description, args.state)
            case "rm":
                result_msg = rm(tasklist, args.task_id)
            case "show":
                result_msg = show(tasklist)

        io.write_tasks(args.path, tasklist)
        io.write_logs(LOG_FILE, action, result_msg)

    except FileNotFoundError:
        print("Task file not found.")
        return False


if __name__ == "__main__":
    main()