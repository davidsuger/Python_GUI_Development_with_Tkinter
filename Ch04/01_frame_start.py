#!/usr/bin/python3
# frame.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

fram = ttk.Frame(root)
fram.pack()

fram.config(height=100, width=200)
fram.config(relief=RIDGE)

ttk.Button(fram, text="Click Me").grid()
fram.config(padding=(30, 15))

ttk.LabelFrame(root, height=100, width=200, text='My Frame').pack()

root.mainloop()
