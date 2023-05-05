#!/usr/bin/env python3
# coding: utf8

import tkinter as tk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("350x200+1000+40")

# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack()

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=15, ipady=5, fill=tk.Y, expand=True)

# box 3
box3 = tk.Label(root, text="Box 3 langer text", bg="blue", fg="white")
box3.pack(expand=True, anchor=tk.E, fill=tk.BOTH)

root.mainloop()