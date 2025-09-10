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

def show(file):
    """
    Displays tasks from a file in a formatted manner.
    Each line in the file should be in the format: id;description
    """
    with open(file, 'r') as text_file:
        lines = text_file.readlines()
        for line in lines:
            print(f"{line.strip().split(';')[0]}: {line.strip().split(';')[1]}")

modify("test.txt","02","task2")
#rm("test.txt","03")
        io.write_tasks(args.path, tasklist)

    except FileNotFoundError:
        print("Task file not found.")
        return False


if __name__ == "__main__":
    main()
