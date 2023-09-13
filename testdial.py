import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as TkFont

class Test_dial(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.canvas1 = tk.Canvas( self, width = 320, height = 320)
        self.canvas1.pack(fill = "both", expand = True)
        self.bg = tk.PhotoImage(file="dial.png")
        self.canvas1.create_image( 1, 0, image = self.bg, anchor = "nw")

        fnt = TkFont.Font(family='Arial', size=24, weight='bold')
        self.textitem = self.canvas1.create_text(150, 270, font=fnt, text="--")

        self.needle = Image.open("needle3.png")
        tkimage = ImageTk.PhotoImage(self.needle.rotate(0))
        self.canvas1.create_image(160,160, image = tkimage, anchor = "nw")
        
        
        
        
if __name__ == "__main__":
    clock = Test_dial()
    clock.mainloop()
        
        
