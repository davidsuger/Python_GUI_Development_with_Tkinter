#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
import textwrap

root = Tk()
button = ttk.Button(root,text = "Click Me")
button.pack()

print(button["text"])
button["text"] = "Press Me"
button.config(text="Push Me")

print(textwrap.fill(str(button.config()),width=70))

print(str(button))

print(str(root))

ttk.Label(root,text="Hello Tkinter!").pack()

root.mainloop()