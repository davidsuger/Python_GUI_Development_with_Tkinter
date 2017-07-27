#!/usr/bin/python3
# toplevel.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *

root = Tk()
window = Toplevel(root)
window.title('New Window')
root.lower(window)

window.state('zoomed')
window.state('withdrawn')
window.state('iconic')
window.state('normal')
window.state('normal')



print(window.state())

window.iconify()
window.deiconify()

window.geometry('640x480+500+100')
window.resizable(False, False)

window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True,True)

window.destroy()
root.destroy()

root.mainloop()
