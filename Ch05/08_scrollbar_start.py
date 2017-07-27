#!/usr/bin/python3
# scrollbar.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()
text = Text(root, width=40, height=10, wrap='word')
text.grid(row=0, column=0)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand=scrollbar.set)

window = Toplevel(root)
canvas = Canvas(window, scrollregion=(0, 0, 640, 480), bg='white')
xscroll = ttk.Scrollbar(window, orient=HORIZONTAL, command=canvas.xview)
yscroll = ttk.Scrollbar(window, orient=VERTICAL, command=canvas.yview)
canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

canvas.grid(row=1, column=0)
xscroll.grid(row=2, column=0, sticky='ew')
yscroll.grid(row=1, column=1, sticky='ns')


def canvas_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='green')


canvas.bind('<1>', canvas_click)

root.mainloop()
