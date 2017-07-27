#!/usr/bin/python3
# pack.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

# ttk.Label(root, text="Hello Tkinter!", background='yellow').pack(fill=BOTH, expand=True)
# ttk.Label(root, text="Hello Tkinter!", background='blue').pack()
# ttk.Label(root, text="Hello Tkinter!", background='green').pack(fill=BOTH, expand=True)
label = ttk.Label(root, text="Hello Tkinter!", background='yellow')
label.pack(side=LEFT, anchor='nw')
print(label)

ttk.Label(root, text="Hello Tkinter!", background='blue').pack(side=LEFT, padx=10, pady=10)
ttk.Label(root, text="Hello Tkinter!", background='green').pack(side=LEFT, ipadx=10, ipady=10)

for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info())

label.pack_forget()

root.mainloop()
