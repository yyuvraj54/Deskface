
from tkinter import *
from PIL import Image, ImageTk


def resizeImage(path, newWidth, newHeight):
    image = Image.open(path) 
    resize_image = image.resize((newWidth, newHeight))
    img = ImageTk.PhotoImage(resize_image)
    return img