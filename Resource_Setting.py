import os
from tkinter import *
from Data import SysInfo


def SetScreen(height,width):
    value=f"{width}x{height}"
    with open('Libs//currentmemory.txt','r') as f:
        newlines=[]
        lines = f.readlines()
        for x in lines:
            newlines.append(x.split()[0])
    newlines[0]=value
    file = open("Libs//currentmemory.txt","w")
    file.seek(0)
    file.close()
    try:
        fa=open('Libs//currentmemory.txt','a')
        fa.seek(0)
        for listitem in newlines:
            fa.write('%s\n' % listitem)
        fa.close()
    except:print("setting up resolution failed!")
    


download=Tk()
height = download.winfo_screenheight()
width = download.winfo_screenwidth()
SetScreen(height,width)
download.title("Deskface-Download")
download.maxsize(400,400)
download.config(bg="white")
Label(download,text="Please wait! while we download some required modules.",fg="grey",bg="white").pack()
changelabel=Label(download,bg="white")
changelabel.pack()

def exit():
    download.destroy()
Exitbut=Button(download,text="Exit",command=exit)
Exitbut.pack()


    
def check_internet():
    import urllib.request
    host='http://google.com'
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False


value=check_internet()
if (value):
    changelabel.config(text="Internet Connected")
    changelabel.config(text="Downloading Fiels")
    system=SysInfo.getSystemOS()
    if system=="MacOs":
        changelabel.config(text="Installing Pillow-file if not installed...")
        print("Installing Pillow-file if not installed...")
        try:
            from PIL import Image, ImageFont, ImageDraw 
        except ImportError:
            os.system('python3 -m pip install Pillow')
        except ModuleNotFoundError:
            os.system('python3 -m pip install Pillow')

        
        changelabel.config(text="Done Installing")
        print("Done Installing Loading Main Screen")
        download.destroy()




    else:
        changelabel.config(text="Installing Pillow-file if not installed...")
        print("Installing Pillow-file if not installed...")    
        try:
            from PIL import Image, ImageFont, ImageDraw 
        except ModuleNotFoundError:
            os.system('python -m pip install Pillow')
        except ImportError:
            os.system('python -m pip install Pillow')



        changelabel.config(text="Done Installing")
        print("Done Installing Loading Main Screen")
        download.destroy()
else:
    changelabel.config(text="No Internet Connection Found")





download.mainloop()