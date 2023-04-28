# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets

import os

from b2_frame_base import FrameBase


class FileSystemFrame(FrameBase):

    def __init__(self, container):
        super().__init__(container, "File System")

    def handle_item_double_clicked(self, event):
        """handler when a list item is double clicked: changes the current path accordingly or open it if its a file."""

        # fetch current selected item
        selected_index = self.list_box.curselection()
        selected_item = self.list_box.get(selected_index)
        if os.path.isdir(selected_item):
            # change working directory if its a directory
            os.chdir(selected_item)
            self.handle_path_changed()
        else:
            # if its a file, open it.
            # TODO: make this more platform independent.
            if selected_item.endswith(".py"):
               os.system(f'notepad "{selected_item}"') # do not start Python files, show them with notepad
            else:
                os.system(f'"{selected_item}"') # open / start files with program associated with it. Wrap path in double quotes.


    def setup(self):
        self.list_items = tk.Variable()

        primary_frame = widgets.Frame(self)
        self.borderize(primary_frame, tk.GROOVE)
        primary_frame.pack(fill=tk.X)

        # create and configure label which shows the current path
        self.path_label = widgets.Label(primary_frame)
        self.path_label.pack(fill=tk.X)

        # create and configure the 'file browser' list box
        self.list_box = tk.Listbox(primary_frame, listvariable=self.list_items)
        self.list_box.pack(fill=tk.BOTH, expand=True)
        self.list_box.bind('<Double-1>', self.handle_item_double_clicked) # connect the double click event to our handler 

        self.handle_path_changed()


    def handle_path_changed(self):
        """Updates the list_box and the path_label"""
        # retrieve and set all file items (directories and files) of the current working directory
        cwd = os.getcwd()
        items = os.listdir()
        items.insert(0, '..')
        self.list_items.set(items)

        self.path_label['text'] = cwd

        # change foreground to blue for all directories
        for i in range(len(items)):
            if os.path.isdir(items[i]):
                self.list_box.itemconfig(i, foreground="blue")
            else:
                self.list_box.itemconfig(i, foreground="black")
