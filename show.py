format = "id;description"

def show(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(f"{line.strip().split(';')[0]}: {line.strip().split(';')[1]}")

show("test.txt")
            
              
