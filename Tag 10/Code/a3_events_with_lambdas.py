#!/usr/bin/env python3
# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets
import tkinter.messagebox as msgs

def handle_button_command(button_name):
    msgs.showinfo(message="command handler invoked for button "+button_name)

def handle_button_event(event):
    if event.num == 3:
        msgs.showinfo(message=f"event handler: {event}")
    else:
        msgs.showinfo(message=f"not right mouse button")

def handle_button_return(event_args):
    msgs.showinfo(message=f"event handler <return>: {event_args}")

# root window
root = tk.Tk()
root.geometry("240x100+1000+40")
root.title('Event Demo')


# Add and configure two buttons
widgets.Button(root, text="Click Me 1", command=lambda: handle_button_command("btn 1")).pack()
widgets.Button(root, text="Click Me 2", command=lambda: handle_button_command("btn 2")).pack()
widgets.Button(root, text="Click Me 3", command=lambda: handle_button_command("btn 3")).pack()
btn = widgets.Button(root, text="Click Me 4")
btn.bind('<Button>', handle_button_event)
btn.bind('<Return>', handle_button_return)
btn.pack()

root.mainloop()