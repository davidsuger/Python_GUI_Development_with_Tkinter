#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
import time

root = Tk()
button = ttk.Button(root, text="Click Me")
button.pack()


def callback():
    print('Clicked!')
    button.state(['!focus'])


button.config(command=callback)
button.invoke()
button.state(['disabled'])
print(button.instate(['disabled']))
button.state(['!disabled'])
button.state(['focus'])

logo = PhotoImage(file='python_logo.gif')
button.config(image=logo, compound='left')
small_logo=logo.subsample(5,5)
button.config(image=small_logo, compound='left')


root.mainloop()
