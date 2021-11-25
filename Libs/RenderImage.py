from PIL import Image, ImageFont, ImageDraw 
from Libs import ImageResize
import pathlib
from datetime import datetime
import os





def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)



def PercentToScreenSize(ss,objx,objy):   #ss look like this-"1440x900"
  #xy=ss.split("x")
  w=2560
  h=1600
  wp=int(w)*(objx/100)
  xp=int(h)*(objy/100)
  return (int(wp),int(xp))


#   title- [ Titletext , fontfamily , size , color , cordinate x , cordinate y ]
#   cap- [Captext , fontfamily , size , color , cordinate x , cordinate y ]
#   logo- [logoPath , cordinate x , cordinate y]

def ProcessImage(Path,title,cap,logo,screenSize,ImageNeeded,set,user):
  try:
    titlefont=title[1]
    titleSize=int(title[2])

    capfont=cap[1]
    capSize=int(cap[2])

    titlecord=PercentToScreenSize(screenSize,title[4],title[5])
    capcord=PercentToScreenSize(screenSize,cap[4],cap[5])

    
    
    
    my_image =Image.open(Path)
    my_image=my_image.resize((2560,1600))
    



    if logo!=[] and ImageNeeded:
      logocoed=PercentToScreenSize(screenSize,logo[1],logo[2])
      logoimage=Image.open(logo[0])
      wi,he,=my_image.size
      logoW,logoH=logoimage.size
      logoimage=logoimage.resize((logoW+100,logoH+100))
      
      tupleforcorrdinate=(logocoed[0], logocoed[1])
      my_image.paste(logoimage,tupleforcorrdinate )
  

    
    title_font = ImageFont.truetype(titlefont,titleSize+80)
    cap_font = ImageFont.truetype(capfont, capSize+80)
    
    title_text = title[0]
    cap_text = cap[0]

    image_editable = ImageDraw.Draw(my_image)


    colortitle=(title[3].split("#"))[1]
    titlecolor=hex_to_rgb(colortitle)
    image_editable.text((titlecord[0],titlecord[1]), title_text, titlecolor,font=title_font)


    colorcap=(cap[3].split("#"))[1]
    capcolor=hex_to_rgb(colorcap)
    image_editable.text((capcord[0],capcord[1]), cap_text, capcolor,font=cap_font)

    now = str(datetime.now())
    desktop = pathlib.Path.home() / 'Desktop'
    now.replace(":","-")

    

    def set_desktop_background(filename):
      import subprocess
      SCRIPT = """/usr/bin/osascript<<END
        tell application "Finder"
        set desktop picture to POSIX file "{}"
        end tell
        END"""  
      subprocess.Popen(SCRIPT.format(filename), shell=True)
      



    if title[0]=="":
      title[0]="Unknown"
    if set: # Want to set wallpaper
      

      if user=="MacOs":
        my_image.save(f"{desktop}//{title[0]}.png",quality=95)
        set_desktop_background(f"{desktop}//{title[0]}.png")
      else:
        import ctypes
        my_image.save(f"{desktop}\\{title[0]}.png",quality=95)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{desktop}\\{title[0]}.png" , 0)
    
    else: # Want to just save file
      if user=="MacOs":
        my_image.save(f"{desktop}//{title[0]}.png",quality=95)
      else:
        my_image.save(f"{desktop}\\{title[0]}.png",quality=95)


  except(ModuleNotFoundError):print("Image Processing Error Try Other background,font,size etc.")

if __name__=="__main__":
    pass