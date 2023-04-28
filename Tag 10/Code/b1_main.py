#!/usr/bin/env python3
# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets
from b3_datetime_frame import DateTimeFrame
from b4_filesystem_frame import FileSystemFrame

def main():
    # root window
    root = tk.Tk()
    root.geometry('400x300+1000+40')
    root.title('Demo GUI')
    root.iconbitmap('./Code/Resources/Icon.ico')

     # create a notebook
    notebook = widgets.Notebook(root)
    notebook.pack(expand=True, fill=tk.BOTH)

    # create the different frames and add them to the notebook (aka 'tabs')
    frames = [DateTimeFrame(notebook), FileSystemFrame(notebook)]

    for frame in frames:
        notebook.add(frame, text=frame.caption)

    root.mainloop()

if __name__ == '__main__':
    main()


