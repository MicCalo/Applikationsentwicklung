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
root.columnconfigure(1, weight=5)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

tk.Label(root, text="A1", bg="blue").grid(column=0, row=0, padx=5, sticky=tk.EW)
tk.Label(root, text="B1", bg="green").grid(column=1, row=0, sticky = 'EW')
widgets.Label(root, text="A2 länger längerlängerlänger").grid(column=0, row=1)
widgets.Label(root, text="B2").grid(column=1, row=1)

root.mainloop()