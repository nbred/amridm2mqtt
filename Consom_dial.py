import os
import sys
import time
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as TkFont
from tkinter import ttk

class Consom_dial(tk.Tk):
    # scale of 30
    scale1 = 0.0
    scale2 = 0.0
    value = 0.0
    canvas_obj = None
    Master = None
    
    def __init__(self, root) -> None:
        super().__init__()
        self.Master = root
        # Add background image file
        self.bg = tk.PhotoImage(file="dial.png")
        # Create Canvas
        self.canvas1 = tk.Canvas( root, width = 320, height = 320)
        self.canvas1.pack(fill = "both", expand = True)
        # Display background
        self.canvas1.create_image( 1, 0, image = self.bg, anchor = "nw")

        # create text item
        fnt = TkFont.Font(family='Arial', size=24, weight='bold')
        self.textitem = self.canvas1.create_text(150, 270, font=fnt, text="--")

        # Create Needle
        self.needle = Image.open("needle3.png")
        
        #self.canvas1.update()
        #self.Master.after(1000, self.SetDialValue(10))
    
    def getAnAngle(self, v):
        return round(self.scale1 * v,1)

    def SetScales(self, v):
        self.scale1 = 273 / v
        self.scale2 = v / 273
        
    def SetDialValue(self, v):
        #self.value = v
        self.value = self.getAnAngle(v)
        angle = 135 - self.value
        if self.canvas_obj != None:
            self.canvas1.delete(self.canvas_obj)
        tkimage = ImageTk.PhotoImage(self.needle.rotate(angle))
        self.canvas_obj = self.canvas1.create_image(160, 160, image=tkimage)    
        self.canvas1.itemconfigure(self.textitem, text=round(self.value*self.scale2,1))
        #self.Master.after(1000, self.SetDialValue(20))
        
        
