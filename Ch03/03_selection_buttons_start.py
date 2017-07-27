#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

checkButton = ttk.Checkbutton(root, text='SPAM?')
checkButton.pack()

spam = StringVar()
spam.set('SPAM!')
print(spam.get())

checkButton.config(variable=spam, onvalue='SPAM Please!', offvalue='Boo SPAM')


def callback():
    print(spam.get())


checkButton.config(command=callback)

breakfast = StringVar()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()

checkButton.config(textvariable = breakfast)

root.mainloop()
