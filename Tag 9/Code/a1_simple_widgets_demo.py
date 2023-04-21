#!/usr/bin/env python3
# coding: utf8


import tkinter as tk
import tkinter.ttk as widgets


def main():
    root = tk.Tk()

    setup_main_window(root) 

    # Label
    widgets.Label(root, text="Label").grid(column=0, row=0, sticky=tk.W)
    widgets.Label(root, text="This is a label").grid(column=1, row=0, sticky=tk.W)

    # Button
    widgets.Label(root, text="Button").grid(column=0, row=1, sticky=tk.W)
    widgets.Button(root, text="Click me!").grid(column=1, row=1, sticky=tk.W)

    # Checkbox
    widgets.Label(root, text="Checkbox").grid(column=0, row=2, sticky=tk.W)
    widgets.Checkbutton(root, text="Choose me!").grid(column=1, row=2, sticky=tk.W)

    #  buttons share a StringVar as group (only one is selected)
    radiobutton_value = tk.StringVar()
    widgets.Label(root, text="Radio buttons").grid(column=0, row=3, sticky=tk.W)
    widgets.Radiobutton(root, text="good choice", value='1',
                        variable=radiobutton_value).grid(column=1, row=3, sticky=tk.W)
    widgets.Radiobutton(root, text="better choice", value='2',
                        variable=radiobutton_value).grid(column=1, row=4, sticky=tk.W)

    # Textinput
    widgets.Label(root, text="Textfield").grid(column=0, row=5, sticky=tk.W)
    widgets.Entry(root).grid(column=1, row=5, sticky=tk.W)

    # Spinbox
    widgets.Label(root, text="Spinbox").grid(column=0, row=6, sticky=tk.W)
    widgets.Spinbox(root).grid(column=1, row=6, sticky=tk.W)

    # Combobox / Dropdown
    widgets.Label(root, text="Combobox").grid(column=0, row=7, sticky=tk.W)
    widgets.Combobox(root, values=["option 1", "option 2"]).grid(column=1, row=7, sticky=tk.W)

    # Slider
    widgets.Label(root, text="Slider").grid(column=0, row=8, sticky=tk.W)
    widgets.Scale(root).grid(column=1, row=8, sticky=tk.W)

    setup_background(root)

    # run the app
    root.mainloop()

def setup_main_window(root: tk.Tk):
    # setup main window
    root.title("Widgets")
    root.iconbitmap('./Code/Resources/Icon.ico')

    # layout (grid, 2x9)
    root.columnconfigure(0)
    root.columnconfigure(1, weight=1)

    for r in range(9):
        root.rowconfigure(r, weight=1, minsize=20)

def setup_background(root: tk.Tk):
    # set background were possible
    root['background'] = 'white'
    for child in root.children.values():
        try:
            child['background'] = 'white'
        except:
            pass


if __name__ == '__main__':
    main()
