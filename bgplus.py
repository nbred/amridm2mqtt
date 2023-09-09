# Import module
import tkinter as tk
import time
from PIL import Image, ImageTk
import tkinter.font as TkFont

# scale of 30
scale1 = 273 / 30
scale2 = 30 / 273
canvas_obj = 0

def getAnAngle(v):
    global scale1
    return round(scale1 * v,1)

# Create object
root = tk.Tk()
# Adjust size
root.geometry("322x322")

# Add background image file
bg = tk.PhotoImage(file="dial.png")
# Create Canvas
canvas1 = tk.Canvas( root, width = 320, height = 320)
canvas1.pack(fill = "both", expand = True)
# Display background
canvas1.create_image( 1, 0, image = bg, anchor = "nw")

# create text item
fnt = TkFont.Font(family='Arial', size=24, weight='bold')
textitem = canvas1.create_text(150, 270, font=fnt, text="")

# Create Needle
needle = Image.open("needle3.png")

for v in range(31):
    value = getAnAngle(v)
    angle = 135 - value
    if canvas_obj != 0:
        canvas1.delete(canvas_obj)
    tkimage = ImageTk.PhotoImage(needle.rotate(angle))
    canvas_obj = canvas1.create_image(160, 160, image=tkimage)    
    canvas1.itemconfigure(textitem, text=round(value*scale2,1))
    canvas1.update()
    time.sleep(1)

# print(TkFont.families())
# Execute tkinter
root.mainloop()
