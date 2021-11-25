from tkinter import *
from tkinter.font import Font
from typing import DefaultDict
from Data import SysInfo
from tkinter import ttk
from Libs import ImageResize
from threading import   Thread
from tkinter import filedialog
from Libs import Load
import os
from Libs import SoftwareMemoryLoader
from Libs import RenderImage
import math




# Page Height and Width
myheight=700
mywidth=1000

# Tkinter Window Setup
home=Tk()
home.title("Deskface")
home.minsize(mywidth,myheight)
home.maxsize(mywidth,myheight)
home.config(bg="white")


#Logo of window
photo = PhotoImage(file = "Data//SystemOs//DeskfaceLogo.png")
home.iconphoto(False, photo)


#Getting Font,color,size for Deskface
Memorybank=SoftwareMemoryLoader.getlook()
ImageNeeded=False
BottomTheme="white"




# Frame for main background image (All main opration)
WallpaperFrame=Frame(home)
WallpaperFrame.pack(fill=X,anchor=NW)



# Create a Canvas Window

canvasheight=500
mycanvas=Canvas(WallpaperFrame, height=canvasheight, width=mywidth)
mycanvas.pack()

#Setting Background Image in Canvas
backgroundWallpaper="Data//SolidColors//Turquoise Green.png"
wallname="Turquoise Green.png"
backgroundCanvas= ImageResize.resizeImage(f"Data//SolidColors//{wallname}",  mywidth,myheight)
wallpaper=mycanvas.create_image(0,0,image=backgroundCanvas ,anchor="nw")




# >>>>>>>>>>> Main bottom Frame  (All buttons and wiged) <<<<<<<<<<<<<<<<




ToolFrame=Frame(home,bg=BottomTheme)
ToolFrame.pack(expand=True,fill=BOTH)
#All Stuff related to Bottom Tools

def getSelectedItem(evt):
    global wallname ,backgroundCanvas,backgroundWallpaper
    try:
        w = evt.widget
        index = int(w.curselection()[0])
        wallname = w.get(index)
        backgroundCanvas= ImageResize.resizeImage(f"Data//SolidColors//{wallname}.png",  mywidth,myheight)
        backgroundWallpaper=f"Data//SolidColors//{wallname}.png"
        mycanvas.itemconfig(wallpaper,image=backgroundCanvas)
    except:
        print("Wrong Index Loaded")
    


# Frame for listbox
listboxFrame=Frame(ToolFrame,bg=BottomTheme)
listboxFrame.pack(fill=Y,anchor="nw",padx=10,pady=2,side=LEFT)

#Getting all filesname from solid color directory
solidColorPath= 'Data//SolidColors'
files = os.listdir(solidColorPath)

#Creating listbox and inserting solid color names

Label(listboxFrame,text="Solid Colors",fg="grey",bg=BottomTheme).pack()
listbox=Listbox(
    listboxFrame,
    activestyle = 'dotbox', 
    font = "Helvetica",
    fg = "purple")
for color in files:
    if "png" in color:
        val=color.split(".png")
        listbox.insert(END,val[0])
listbox.pack(fill=Y)

listbox.bind("<<ListboxSelect>>", getSelectedItem)


# If Graphic Selected from listbox
def graphicSelected(ev):
    global wallname ,backgroundCanvas,backgroundWallpaper
    try:
        w = ev.widget
        index = int(w.curselection()[0])
        wallname = w.get(index)
        backgroundCanvas= ImageResize.resizeImage(f"Data//Graphic//{wallname}.png",  mywidth,myheight)
        backgroundWallpaper=f"Data//Graphic//{wallname}.png"
        mycanvas.itemconfig(wallpaper,image=backgroundCanvas)
    except:
        print("Wrong Index Loaded")



# FRAME FOR GRAPHIC BACKGROUND

def importImageNow():
    global backgroundCanvas,backgroundWallpaper

    try:
        filename=filedialog.askopenfilename()
        backgroundCanvas= ImageResize.resizeImage(filename,  mywidth,myheight)
        backgroundWallpaper=filename
        mycanvas.itemconfig(wallpaper,image=backgroundCanvas)
    except:
        print("Image Not Selected / Image should be in png format")

GraphicFrame=Frame(ToolFrame,bg=BottomTheme)
GraphicFrame.pack(anchor="nw",padx=10,pady=2,fill=Y,side=LEFT)

Label(GraphicFrame,text="Graphic Images",fg="grey",bg=BottomTheme).pack()

GraphicImage=Listbox(GraphicFrame,height=7)
GraphicPath = os.listdir("Data/Graphic")

for graphicname in GraphicPath:
    if "png" in graphicname:
        sp=graphicname.split(".png")
        GraphicImage.insert(END,sp[0])
GraphicImage.pack()

def TitleKeyUp(e):
    mycanvas.itemconfigure(Maintitle,text=title.get())
def CapKeyUp(e):
    mycanvas.itemconfigure(MainCap,text=caption.get())

def runthread(ev):
    a_thread = Thread(target =graphicSelected(ev))
    a_thread.start()
    a_thread.join()    

GraphicImage.bind("<<ListboxSelect>>",runthread)

importImage=Button(GraphicFrame,text="Background (PNG) Image",command=importImageNow,bg="#f4c4ca")
importImage.pack(pady=10)



#Frame for Text and Logo to add in main Screen

desktopframe=Frame(ToolFrame,bg=BottomTheme)
desktopframe.pack(fill=Y,side=LEFT,pady=2,padx=10)
Label(desktopframe,text="Edit Tools",fg="grey",bg=BottomTheme).pack()

# Two Entry box first is for title and another is for main caption
title=StringVar()
caption=StringVar()

DefaultTitle="Welcom"
DefaulCap="Enter your Desc"
title.set(DefaultTitle)
caption.set(DefaulCap)

# Canvas Opration>>>>>>>>>>>>>>>>>>>>>>>>>
MainImage=mycanvas.create_image(100,100, anchor=NW)
Maintitle=mycanvas.create_text((mywidth//2)-190,100,fill=Memorybank[1],font=(Memorybank[2],Memorybank[3]),text=DefaultTitle,anchor="nw")
MainCap=mycanvas.create_text((mywidth//2)-170,220,fill=Memorybank[4],font=(Memorybank[5],Memorybank[6]),text=DefaulCap,anchor="nw")
def drag_start(event):
    widget = event.widget
    widget.startX, widget.startY = event.x, event.y
def movTitle(event):
    widget = event.widget
    widget.move(Maintitle, event.x-widget.startX, event.y-widget.startY)
    widget.startX=event.x 
    widget.startY =event.y # update previous position
def movCap(event):
    widget = event.widget
    widget.move(MainCap, event.x-widget.startX, event.y-widget.startY)
    widget.startX, widget.startY = event.x, event.y # update previous position
def movImg(event):
    widget = event.widget
    widget.move(MainImage, event.x-widget.startX, event.y-widget.startY)
    widget.startX, widget.startY = event.x, event.y # update previous position

mycanvas.tag_bind(Maintitle,"<Button-1>",drag_start)
mycanvas.tag_bind(MainCap,"<Button-1>",drag_start)
mycanvas.tag_bind(MainImage,"<Button-1>",drag_start)
mycanvas.tag_bind(Maintitle,'<B1-Motion>',movTitle)
mycanvas.tag_bind(MainCap,'<B1-Motion>',movCap)
mycanvas.tag_bind(MainImage,'<B1-Motion>',movImg)

# Tow frame for writing and editing
writing=Frame(desktopframe,bg=BottomTheme)
writing.pack(fill=Y,anchor="nw",side=LEFT)



#All frame work down for editing and writing (frame-1 writing)

Titlelabel=Label(writing,text="Title:",bg=BottomTheme).pack(anchor="nw")
innertitleframe=Frame(writing)
TitleEntry=Entry(innertitleframe,textvariable=title,bg="#d9f1ff")
TitleEntry.grid(row=0,column=0)

TitleEntry.bind("<KeyRelease>", TitleKeyUp)



innertitleframe.pack(anchor="nw")

Captionlabel=Label(writing,text="Caption:",bg=BottomTheme).pack(anchor="nw")
CaptionEntry=Entry(writing,textvariable=caption,bg="#d9f1ff")
CaptionEntry.pack(anchor="nw")

CaptionEntry.bind("<KeyRelease>", CapKeyUp)


moreandRe=Frame(writing,bg=BottomTheme)
moreandRe.pack(pady=10)
def editnow():
    Load.MoreOptions(MoreEdit,title.get(),caption.get(),mycanvas,MainCap,Maintitle)
MoreEdit=Button(moreandRe,text="More Options",command=editnow)
MoreEdit.pack(side=LEFT)


def recenterit():
    mycanvas.coords(MainCap,(mywidth//2)-170,220)
    mycanvas.coords(Maintitle,(mywidth//2)-190,100)

RecentrButton=Button(moreandRe,text="Recenter Text",command=recenterit)
RecentrButton.pack(side=LEFT)

def percentless(imagew,imageh):
    wallpaperw=2560
    wallpaperh=1600

    x=(imagew*100)/wallpaperw
    y=(imageh*100)/wallpaperh

    width=mywidth*(x/100)
    height=canvasheight*(y/100)

    return (int(width)+40,int(height)+40)

    

logopath=""
def choosesLogo():
    from PIL import ImageTk, Image
    global logo,logopath ,logoImageButton,buttonlogoresize,ImageNeeded,imgPhoto,lg
    try:
        logopath=filedialog.askopenfilename()
        logoImageResize=Image.open(logopath)
        
        wid,hei=logoImageResize.size
        lowsize=percentless(wid,hei)
        lg=logoImageResize.resize(lowsize)        
        imgPhoto = ImageTk.PhotoImage(lg) 
        
        mycanvas.itemconfig(MainImage,image=imgPhoto)
        mycanvas.coords(MainImage,200,200)
        
        try:
            logoImageButton.config(text='')
            buttonlogoresize= ImageResize.resizeImage(logopath,100,100)
            logoImageButton.config(image=buttonlogoresize)
            mycanvas.itemconfig(MainImage, state='normal')
            removeImage.pack()
            note.pack_forget()
            ImageNeeded=True
        except:pass
    except:print("Image Import Error")


editing=Frame(ToolFrame,bg=BottomTheme)
editing.pack(fill=BOTH,anchor="nw",side=LEFT)
Label(editing,text="Add Logo",fg="grey",width=30,bg=BottomTheme).pack()

note=Label(editing,text="No Image(PNG) Selected",fg="black",width=30,bg=BottomTheme)
note.pack()

logoImageButton=Button(editing,text="Upload (PNG) Now",command=choosesLogo,bg=BottomTheme)
logoImageButton.pack(fill=BOTH)
logoImageButton.pack_propagate(0)


def removeImageNow():
    global ImageNeeded
    note.pack()
    removeImage.pack_forget()
    ImageNeeded=False
    mycanvas.itemconfig(MainImage, state='hidden')

    


removeImage=Button(editing,text="Remove Image",command=removeImageNow)
Label(editing,text="Image may not look perfect in preview\nbut will be fine in Saved state",fg="red").pack()




#   title- [ Titletext , fontfamily , size , color , cordinate x , cordinate y ]
#   cap- [Captext , fontfamily , size , color , cordinate x , cordinate y ]
#   logo- [logoPath , cordinate x , cordinate y]
#   (2560,1600)
def calculatePercent(cord):
    x=cord[0]
    y=cord[1]
    xp=(x*100)/mywidth
    yp=(y*100)/canvasheight+3
    return (xp,yp)

def savewall():
    cordOfTitle=mycanvas.coords(Maintitle)
    cordOfCap=mycanvas.coords(MainCap)
    cordOflogo=mycanvas.coords(MainImage)
    
    TitleScreen=calculatePercent(cordOfTitle)
    CapScreen=calculatePercent(cordOfCap)
    

    
    


    lookData=SoftwareMemoryLoader.getlook()   #[ 0,titleColor ,titleFornt ,titleSize , capColor ,capFont, capSize ]

    titleData=[title.get() , lookData[2] , int(lookData[3])+100, lookData[1] ,TitleScreen[0],TitleScreen[1]]
    CapData=[caption.get(), lookData[5] , lookData[6] , lookData[4] ,CapScreen[0],CapScreen[1]]
    if logopath!="":
        LogoScreen=calculatePercent(cordOflogo)
        logoData=[logopath,LogoScreen[0],LogoScreen[1]]
    else:
        logoData=[]

    RenderImage.ProcessImage(backgroundWallpaper,titleData,CapData,logoData,Memorybank[0],ImageNeeded,False,SysInfo.getSystemOS())

    
def setwallpaper():
    
    cordOfTitle=mycanvas.coords(Maintitle)
    cordOfCap=mycanvas.coords(MainCap)
    cordOflogo=mycanvas.coords(MainImage)
    
    TitleScreen=calculatePercent(cordOfTitle)
    CapScreen=calculatePercent(cordOfCap)

    lookData=SoftwareMemoryLoader.getlook()   #[ 0,titleColor ,titleFornt ,titleSize , capColor ,capFont, capSize ]

    titleData=[title.get() , lookData[2] , int(lookData[3])+100, lookData[1] ,TitleScreen[0],TitleScreen[1]]
    CapData=[caption.get(), lookData[5] , lookData[6] , lookData[4] ,CapScreen[0],CapScreen[1]]
    if logopath!="":
        LogoScreen=calculatePercent(cordOflogo)
        logoData=[logopath,LogoScreen[0],LogoScreen[1]]
    else:
        logoData=[]

    RenderImage.ProcessImage(backgroundWallpaper,titleData,CapData,logoData,Memorybank[0],ImageNeeded,True,SysInfo.getSystemOS())



    

infoFrame=Frame(ToolFrame,bg=BottomTheme)
infoFrame.pack(anchor="ne",side=RIGHT,fill=BOTH,padx=10)

Label(infoFrame,text="Info Tab",fg="grey",bg=BottomTheme).pack()

setwall=Button(infoFrame,text="Set wallpaper",command=setwallpaper)
setwall.pack(pady=5)

save=Button(infoFrame,text="Save wallpaper",command=savewall)
save.pack(pady=5)







def aboutdesk():
    about=Toplevel()
    about.minsize(550,580)
    about.title("About")
    about.iconphoto(False, photo)
    Label(about,text="About Deskface").pack()
    Label(about,image=photo).pack()
    Mainlogo=PhotoImage(file="Data//SystemOs//Mainlogo.png")
    
    Label(about,text="Deskface is a software that is made to create instant simple Desktop Wallpaper" ).pack()
    Label(about,image=Mainlogo).pack()
    Label(about,text="Design and Developed by\nYuvraj Singh Yadav").pack()
    about.mainloop()
about=Button(infoFrame,text="About Deskface",command=aboutdesk)
about.pack(pady=5)

# setting up theme as per Oprating system

if SysInfo.getSystemOS()=="MacOs":
    bottomdockResize = ImageResize.resizeImage("Data//SystemOs//MacOs//WhiteDock.png",  mywidth-205,170-115)
    topdockResize= ImageResize.resizeImage("Data//SystemOs//MacOs//Topbar.png",  mywidth,52-30)
    mycanvas.create_image(0,2,image=topdockResize ,anchor="nw")
    mycanvas.create_image((mywidth-(mywidth-205))//2,canvasheight-58,image=bottomdockResize ,anchor="nw")

else:
    bottomdockResize = PhotoImage(file="Data//SystemOs//WindowsOs//bottomWin.png")
    mycanvas.create_image(0,canvasheight-35,image=bottomdockResize ,anchor="nw")

# End Line for main thread
home.mainloop()