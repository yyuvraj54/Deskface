def getlook():
    f=open('Libs//currentmemory.txt','r')
    Memory=[]
    for i in f.readlines():
        Memory.append((i.split("\n"))[0])
    f.close()
    return Memory
