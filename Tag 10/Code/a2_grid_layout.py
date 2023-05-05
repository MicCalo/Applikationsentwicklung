#!/usr/bin/env python3
# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets

# root window
root = tk.Tk()
root.geometry("240x100+1000+40")
root.title('Grid Demo')


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

tk.Label(root, text="A1", bg="blue").grid(column=0, row=0, ipadx=10, sticky=tk.NS)
tk.Label(root, text="B1", bg="green").grid(column=1, row=0,)
tk.Label(root, text="A2", bg="yellow").grid(column=0, row=1, padx=5, sticky=tk.EW)
tk.Label(root, text="B2", bg="red").grid(column=1, row=1, sticky = 'EW')


root.mainloop()