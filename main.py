from numpy import random

def toDict(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    dicti={}
    for i in range(len(lines)):
         dicti[lines[i].split(';',1)[0]] = lines[i].split(';',1)[1]
    return dicti
    
def UpdateFile(file,dicti):
    with open(file, 'w') as f :
        for i in dicti.keys:
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



          
     
