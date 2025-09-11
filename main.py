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

modify("test.txt","02","task2")
#rm("test.txt","03")

          
     
