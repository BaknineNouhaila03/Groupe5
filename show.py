def show(file_path):
    """
    Displays tasks from a file in a formatted manner.
    Each line in the file should be in the format: id;description
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(f"{line.strip().split(';')[0]}: {line.strip().split(';')[1]}")

show("test.txt")
            
              
