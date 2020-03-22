#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

def getprint():
    text = entry.get()
    print(text)

def gtext():
    text = text_box.get('1.0',END)
    print(text)

root = Tk()

# Demo label
# Backgrounds and Foreground colors may take the
# form of red,green,blue, etc. or RGB values such
# as those listed at: https://htmlcolorcodes.com/color-names/
# Width and height may also be customized.
label = Label(
    text="Label",
    fg='#DDA0DD',
    bg='blue',
    width=10,
    height=10
)
label.pack()

# Demo button
# A button can be thought of as a clickable Label
# and is styled similarly.
# Command works with the entry widget introduced next.
button = Button(
    text='Button',
    width=25,
    height=5,
    bg='blue',
    fg='yellow',
    command=getprint
)
button.pack()

# Entry Demo
# Use an entry widget to get a trivial amount of
# text from the user.
# Retrieve text with .get()
# Delete text with .delete()
# Insert text with .insert()
entry = Entry(
    fg='yellow',
    bg='blue',
    width=50
)
entry.pack()

# Text Box Demo
# Create a text box
text_box = Text()
text_box.pack()

# Create a button to click
# Which will call the gtext method to retrieve the text.
get_text_button = Button(root,text='Get Text',command=gtext)
get_text_button.pack()
root.mainloop()
