from Consom_dial import *
from tkinter import ttk
# Create object
root = tk.Tk()
# Adjust size
root.geometry("322x322")
dial = Consom_dial(root)
dial.SetScales(30)
dial.SetDialValue(20)
#root.after(2000, dial.SetDialValue(15))
root.mainloop()