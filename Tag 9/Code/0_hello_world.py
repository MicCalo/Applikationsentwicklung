#!/usr/bin/env python3
# coding: utf8

import tkinter as tk

# create main window. This is usually called 'root'
root = tk.Tk()

# create a label and make it visible with pack
label = tk.Label(root, text="Hello, world!")
label.pack()

# run the program by executing the main loop
print("starting main loop...")
root.mainloop()
print("main loop finished")