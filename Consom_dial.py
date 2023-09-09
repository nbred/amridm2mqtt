# import os
# import sys
# import time
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as TkFont


class Consom_dial(tk.Tk):
    # scale of 30
    scale1 = 0.0
    scale2 = 0.0
    canvas_obj = None
    
    def __init__(self) -> None:
        super().__init__()
        
        # Add background image file
        self.bg = tk.PhotoImage(file="dial.png")
        # Create Canvas
        self.canvas1 = tk.Canvas( self, width = 320, height = 320)
        self.canvas1.pack(fill = "both", expand = True)
        # Display background
        self.canvas1.create_image( 1, 0, image = self.bg, anchor = "nw")

        # create text item
        fnt = TkFont.Font(family='Arial', size=24, weight='bold')
        self.textitem = self.canvas1.create_text(150, 270, font=fnt, text="--")

        # Create Needle
        self.needle = Image.open("needle3.png")
        
        # self.canvas1.update()
        # self.SetScales(30)
        # self.after(1000, self.SetDialValue(10))
    
    def getAnAngle(self, v):
        return round(self.scale1 * v,1)

    def SetScales(self, v):
        self.scale1 = 273 / v
        self.scale2 = v / 273
        
    def SetDialValue(self, v):
        self.value = self.getAnAngle(v)
        self.canvas1.itemconfigure(self.textitem, text=round(self.value*self.scale2,1))
        angle = 135 - self.value
        tkimage = ImageTk.PhotoImage(self.needle.rotate(angle))
        self.canvas1.create_image(160, 160, image=tkimage)    
        
        # self.canvas1.update()
        # self.after(1000, self.SetDialValue(10))
        
        
        
