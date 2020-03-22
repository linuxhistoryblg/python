#!/usr/bin/env python3
'''Create a tk application with an entry widget.'''
try:
    import Tkinter as tk
    import tkFileDialog as filedialog
except ImportError:
    import tkinter as tk

# Create an entry widget and insert some textvariable
def print_name(arg):
    name = ent_name.get()
    ent_name.delete(0,tk.END)
    ent_name.insert(0,'Hello there, '+ name)

window = tk.Tk()
window.title('Ex2')
ent_name = tk.Entry(width=40)
ent_name.insert(0,'Enter your name and press <Return>')
ent_name.pack()
ent_name.bind('<Enter>', lambda e: ent_name.configure(ent_name.delete(0,tk.END)))
ent_name.focus()
ent_name.bind('<Return>',print_name)
window.mainloop()
