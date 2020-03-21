#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from os import system
import sys

root = Tk()
root.title('RUNIT')
# root.wm_attributes('-type', 'splash')
# root.wm_attributes('-type','dock')
# root.overrideredirect(1)
root.resizable(0, 0)
root.eval('tk::PlaceWindow . center')


def runit(*args):
    root.destroy()
    system(cmd.get())


mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Button(mainframe, text='QUIT', command=root.quit).grid(row=1, column=1, sticky=(S, E))
ttk.Button(mainframe, text='OK', command=lambda: runit()).grid(row=1, column=0, sticky=(S, W))

cmd = StringVar()
cmd_entry = ttk.Entry(mainframe, width=7, textvariable=cmd)
cmd_entry.grid(column=0, row=0, columnspan=2, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
cmd_entry.focus()
root.bind('<Return>', runit)
root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()
