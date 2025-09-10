from numpy import random

def toDict(file):
    dicti={}
    with open(file, 'r') as f:
        for l in f :
         l= l.strip()
         key, value = l.split(";", 1)
         dicti[key]=value
    return dicti
    
def UpdateFile(file,dicti):
    with open(file, 'w') as f :
        for i in dicti.keys():
             f.write(i+";"+dicti[i]+'\n')

def rm(file,id):
    dicti=toDict(file)
    if id in dicti.keys():
        del dicti[id]
        UpdateFile(file,dicti)
    else:
         print("id does not exist ")

def modify(file, id, contenu):
    dicti = toDict(file) 
    if id in dicti.keys():
        dicti[id] = contenu
        UpdateFile(file, dicti)
    else:
        print("id does not exist")

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

          
     
