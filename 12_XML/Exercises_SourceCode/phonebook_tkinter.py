#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
A trivially simple phone book manager.
'''

try:
    from tkinter import Tk, Button, Entry, Frame, IntVar, Label, StringVar
except:
    from Tkinter import Tk, Button, Entry, Frame, IntVar, Label, StringVar

import phonedata

__author__ = 'Russel Winder'
__version__ = '1.0'
__date__ = '2012-02-19'
__copyright__ = 'Copyright © 2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'


class Phonebook (object):
    def __init__(self):
        dataEntry = Frame()
        Label(dataEntry, text='Name').grid(column=0, row=0)
        self.name = StringVar()
        Entry(dataEntry, textvariable=self.name).grid(column=1, row=0)
        Label(dataEntry, text='Number').grid(column=0, row=1)
        self.number = StringVar()
        Entry(dataEntry, textvariable=self.number).grid(column=1, row=1)
        buttons = Frame()
        Button(buttons, text='Add').grid(column=0, row=0)
        Button(buttons, text='Update').grid(column=1, row=0)
        Button(buttons, text='Delete').grid(column=2, row=0)
        dataDisplay = Frame()
        i = 0
        for name, number in phonedata.data.items():
            Label(dataDisplay, text=name).grid(column=0, row=i)
            Label(dataDisplay, text='    ').grid(column=1, row=i)
            Label(dataDisplay, text=number).grid(column=2, row=i)
            i += 1
        padding = 10
        dataEntry.pack(padx=padding, pady=padding)
        buttons.pack(padx=padding, pady=padding)
        dataDisplay.pack(padx=padding, pady=padding)

if __name__ == '__main__':
    root = Tk()
    root.title('Phonebook')
    Phonebook()
    root.mainloop()
