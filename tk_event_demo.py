#!/usr/bin/env python3
import tkinter as tk

root = tk.Tk()
root.title('Keypress Events')

# Create a keypressedlabel
lbl_keypressed = tk.Label(master=root, text='keypressed:', width=10, anchor=tk.E)
lbl_keypressed.grid(row=0, column=0, padx=5, pady=5, sticky='e')

# Create a last 10 keys pressed label
lbl_lastten = tk.Label(master=root, text='Last 10 Keys Pressed:', anchor=tk.E)
lbl_lastten.grid(row=1, column=0, padx=5, pady=5, sticky='e')

# Create a last 10 keys display
lbl_display = tk.Label(master=root, text='', anchor=tk.E)
lbl_display.grid(row=1, column=1, padx=5, pady=5, sticky='e')

# Create an entry box
ent_keypressed = tk.Entry(master=root, width=20)
ent_keypressed.grid(row=0, column=1, padx=5, pady=5)

# Create an exit button
btn_exit = tk.Button(master=root, text='Exit', command=lambda: root.destroy())
btn_exit.grid(row=2, columnspan=2)


# Handle events
def handler(event):
    '''Handle key presses.
    display in ent_keypresed and
    add to last ten keys display'''
    ent_keypressed.delete(0, tk.END)
    ent_keypressed.insert(0, event.char)
    keys = lbl_display['text']
    if len(keys) <= 0:
        lbl_display['text'] = event.char
    elif len(keys) > 9:
        lbl_display['text'] = keys[1:] + event.char
    else:
        lbl_display['text'] = keys + event.char

def ent_handler(event):
    ent_keypressed.delete(0, tk.END)
    ent_keypressed.insert(0, 'Type, don\'t click!')


# Bind keypresses to a handler
root.bind('<Key>', handler)

# Bind mouse clicks to a handler
ent_keypressed.bind('<Button-1>', ent_handler)

# enter mainloop
root.mainloop()
