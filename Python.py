import numpy as np
import cv2
from PIL import ImageGrab
from tkinter import *

master = Tk()
master.title("Screen Capture")
master.geometry("225x25")

def Capture(): 
   img = ImageGrab.grab()
   print (img.show())
   img.save("capture.png")

sent = Button(master, bg="#00aeff",fg="White" , text="Capture", command=Capture)
sent.pack()

master.mainloop()
