#!/usr/bin/python3
# entry.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry.pack()

entry.delete(0, END)
entry.insert(0, 'Enter your password')
print(entry.get())
entry.config(show='*')

entry.state(['disabled'])
entry.state(['!disabled'])
entry.state(['readonly'])

root.mainloop()
