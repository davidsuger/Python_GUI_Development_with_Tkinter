#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk


class Feedback:
    def __init__(self, master):
        master.geometry('480x360+200+200')

        master.title("Explore California Feedback")

        self.frame = ttk.Frame(master)
        self.frame.pack()

        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.frame, image=self.logo).grid(row=0, column=3)
        ttk.Label(self.frame).grid(row=1, column=3)

        ttk.Label(self.frame, text='Name: ').grid(row=2, column=2, stick='e')
        self.entryName = ttk.Entry(self.frame)
        self.entryName.grid(row=2, column=3, stick='w')

        ttk.Label(self.frame, text='Email: ').grid(row=3, column=2, stick='e')
        self.entryEmail = ttk.Entry(self.frame)
        self.entryEmail.grid(row=3, column=3, stick='w')

        ttk.Label(self.frame, text='Comments: ').grid(row=4, column=2, stick='e')

        self.text = Text(self.frame, width=40, height=10)
        self.text.grid(row=5, column=3, columnspan=2)

        self.clearButton = ttk.Button(self.frame, text='Clear')
        self.clearButton.grid(row=6, column=3, stick='w')
        self.submitButton = ttk.Button(self.frame, text='Submit')
        self.submitButton.grid(row=6, column=4, stick='e')

        def clearAllData():
            self.entryName.delete('0', 'end')
            self.entryEmail.delete('0', 'end')
            self.text.delete('1.0', 'end')

        def submitData():
            print('Name: {}'.format(self.entryName.get()))
            print('Email: {}'.format(self.entryEmail.get()))
            print('Comments: {}'.format(self.text.get('1.0', 'end')))
            clearAllData()
            from tkinter import messagebox
            messagebox.showinfo(title='A Friendly Message', message='Your comments submited, Thank you!')

        self.clearButton.config(command=clearAllData)
        self.submitButton.config(command=submitData)


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()
