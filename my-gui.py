#! /usr/bin/env python3

import tkinter as tk

class Application(tk.Frame):

    renameButton = True

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn_start = tk.Button(self)
        self.btn_start["width"] = 12
        self.btn_start["text"] = "Start..."
        self.btn_start["command"] = self.doWork
        self.btn_start.pack(side="top")

        self.btn_quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.btn_quit["width"] = 12
        self.btn_quit.pack()

        self.text_box = tk.Text(self,height=2, width=35)
        self.text_box.pack(side="bottom")
        self.text_box.insert(1.0, "Welcome")

    def doWork(self):
        if (self.renameButton):
             self.btn_start["text"] = "Running..."
             self.renameButton = False

        self.after(900000,self.doWork) # 15 minutes
            
root = tk.Tk()
root.geometry("300x100")
root.title("My GUI")
app = Application(master=root)
app.mainloop()
print("goodbye")

