from tkinter import font
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import colorchooser
from Libs import SoftwareMemoryLoader
from PIL import ImageFont
from tkinter import filedialog




def fontname():
    fontnames=[]
    for fontstyle in font.families():
        try:
            ImageFont.truetype(fontstyle)
            fontnames.append(fontstyle)
        except:pass
    return fontnames

def SaveAllDetails(resolution,colortitle,fonttitle,sizetitle,colorcap,fontcap,sizecap):

    memory=[resolution,colortitle,fonttitle,sizetitle,colorcap,fontcap,sizecap]
    file = open("Libs//currentmemory.txt","w")
    file.seek(0)
    file.close()
    try:
        fa=open('Libs//currentmemory.txt','a')
        for listitem in memory:
            fa.write('%s\n' % listitem)       
        fa.close()
    except:print("Error while Saving Memory")



def MoreOptions(but,titletext,captext,mycanvas,cap,title):

    BackTheme="white"

    DefaultMemory=SoftwareMemoryLoader.getlook()
    resolution=DefaultMemory[0]
    

    defaultTitleColor=DefaultMemory[1]
    defaultCapColor=DefaultMemory[4]

    if titletext=="":
        titletext="No Title Written"
    if captext=="":
        captext="No Caption Written Please Write in main Window of Deskface"

    but.config(state=DISABLED)
    edit=Toplevel()
    edit.config(bg=BackTheme)
    edit.title("Edit Deskface")
    edit.maxsize(380,360)
    edit.minsize(380,360)


    

    def updatePreview(ColorofTitle,SizeofTitle,FontforTitle,ColorofCap,SizeofCap,FontforCap):
        try:
            mycanvas.itemconfig(cap,font=(FontforCap,SizeofCap),fill=ColorofCap)
            mycanvas.itemconfig(title,font=(FontforTitle,SizeofTitle),fill=ColorofTitle)
        except:
            print("Invalid Entry")
    def up(e):
        SaveAllDetails(resolution,Pickcolor["text"],fontfamily.get(),titlefontsize.get(),Pickcolorforcap["text"],fontfamilyforCap.get(),Capfontsize.get())
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())

    def applyit():
        SaveAllDetails(resolution,Pickcolor["text"],fontfamily.get(),titlefontsize.get(),Pickcolorforcap["text"],fontfamilyforCap.get(),Capfontsize.get())
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())
        but.config(state=NORMAL)
        edit.destroy()

    def colorchoosefortitle():
        global ColorofTitle
        ColorofTitle=(colorchooser.askcolor())[1]
        if ColorofTitle=="white":
            Pickcolor.config(text=ColorofTitle,bg="black",fg=ColorofTitle)    
        else:
            Pickcolor.config(text=ColorofTitle,fg=ColorofTitle,bg="white")
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())

    def colorchooseforCap():
        global ColorofCap
        ColorofCap=(colorchooser.askcolor())[1]
        if ColorofCap=="white":
            Pickcolorforcap.config(text=ColorofCap,bg="black",fg=ColorofCap)    
        else:
            Pickcolorforcap.config(text=ColorofCap,fg=ColorofCap,bg="white")
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())


    def stateofbut():
        SaveAllDetails(resolution,Pickcolor["text"],fontfamily.get(),titlefontsize.get(),Pickcolorforcap["text"],fontfamilyforCap.get(),Capfontsize.get())
        but.config(state=NORMAL)
        edit.destroy()

    def Capsizzeup(e):
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())

    def Titlesizeup(e): 
        
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())

    
    def importfontTitle():
        pickedFontTitle=filedialog.askopenfilename(filetypes=[('TrueType','*.ttf')])
        fontfamily.set(pickedFontTitle)
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())
        
    def importfontCap():
        pickedFontCap=filedialog.askopenfilename(filetypes=[("TrueType",'*.ttf')])
        fontfamilyforCap.set(pickedFontCap)
        updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())
        

    edit.protocol("WM_DELETE_WINDOW", stateofbut)
    Label(edit,text="Title Settings",bg="skyblue",fg="grey").pack(anchor="nw",pady=5,padx=5)
    Titleset=Frame(edit)
    Titleset.pack(fill=X,pady=10,anchor="nw")
    
   
    Label(Titleset,text="FontFamily:",bg=BackTheme).grid(row=0,column=0,sticky=NW)
    Label(Titleset,text="Colour Code:",bg=BackTheme).grid(row=1,column=0,sticky=NW,pady=3)
    Label(Titleset,text="Font Size:",bg=BackTheme).grid(row=2,column=0,sticky=NW,pady=3)   

    fontnames=fontname()
    fontfamily=Combobox(Titleset,values=fontnames)
    fontfamily.set(DefaultMemory[2])
    fontfamily.grid(row=0,column=1)
    fontfamily.bind("<<ComboboxSelected>>",up)


    ChooseFontforTitle=Button(Titleset,text="Import Font",bg=BackTheme,command=importfontTitle)
    ChooseFontforTitle.grid(row=0,column=2,padx=2)

    Pickcolor=Button(Titleset,text=defaultTitleColor,width=10,command=colorchoosefortitle,fg=defaultTitleColor,bg=BackTheme)
    Pickcolor.grid(row=1,column=1,sticky="nw",pady=5)

    titlefontsize=StringVar()
    titlefontsize.set(DefaultMemory[3])
    fonttitlesize=Entry(Titleset,width=5,textvariable=titlefontsize,bg=BackTheme)
    fonttitlesize.grid(row=2,column=1,sticky="nw",pady=3)

    fonttitlesize.bind("<KeyRelease>", Titlesizeup)

    #>>>>>>>>>>>>>>>>> Caption Setting <<<<<<<<<<<<<<<<<<<<<#

    Label(edit,text="Caption Settings",bg="skyblue",fg="grey").pack(anchor="nw",pady=5,padx=5)
    Capset=Frame(edit)
    Capset.pack(fill=X,anchor="nw")



    Label(Capset,text="FontFamily:",bg=BackTheme).grid(row=0,column=0,sticky=NW)
    Label(Capset,text="Colour Code:",bg=BackTheme).grid(row=1,column=0,sticky=NW,pady=3)
    Label(Capset,text="Font Size:",bg=BackTheme).grid(row=2,column=0,sticky=NW,pady=3)   

    fontfamilyforCap=Combobox(Capset,values=fontnames)
    fontfamilyforCap.set(DefaultMemory[5])
    fontfamilyforCap.grid(row=0,column=1)
    fontfamilyforCap.bind("<<ComboboxSelected>>",up)

    ChooseforCap=Button(Capset,text="Import Font",bg=BackTheme,command=importfontCap)
    ChooseforCap.grid(row=0,column=2,padx=2)

    Pickcolorforcap=Button(Capset,text=defaultCapColor,width=10,command=colorchooseforCap,fg=defaultCapColor,bg=BackTheme)
    Pickcolorforcap.grid(row=1,column=1,sticky="nw",pady=5)


    Capfontsize=StringVar()
    Capfontsize.set(DefaultMemory[6])
    fontCapsize=Entry(Capset,width=5,textvariable=Capfontsize,bg=BackTheme)
    fontCapsize.grid(row=2,column=1,sticky="nw",pady=3)

    fontCapsize.bind("<KeyRelease>", Capsizzeup)
    


    BottonFrameFroButtons=Frame(edit,bg=BackTheme)
    BottonFrameFroButtons.pack(pady=10)

    Applybutton=Button(BottonFrameFroButtons,text="Apply Change",command=applyit,bg=BackTheme)
    Applybutton.pack(side=RIGHT)
    Label(edit,text="Imported Font are not supported for preview!",bg=BackTheme,fg="red").pack()


    #updatePreview(Pickcolor["text"],titlefontsize.get(),fontfamily.get(),Pickcolorforcap["text"],Capfontsize.get(),fontfamilyforCap.get())




















    edit.mainloop()    