#!/usr/bin/env python3
# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets
import tkinter.messagebox as msgs

def handle_button_command():
    msgs.showinfo(message="command handler invoked")

def handle_button_event(event):
    msgs.showinfo(message=f"event handler: {event}")

def handle_button_return(event_args):
    msgs.showinfo(message=f"event handler <return>: {event_args}")

# root window
root = tk.Tk()
root.geometry("240x100+1000+40")
root.title('Event Demo')


# Add and configure two buttons
widgets.Button(root, text="Click Me", command=handle_button_command).pack()
btn = widgets.Button(root, text="Click Me")
btn.bind('<Button>', handle_button_event)
btn.bind('<Return>', handle_button_return)
btn.pack()

root.mainloop()