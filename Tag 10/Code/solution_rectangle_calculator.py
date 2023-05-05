import tkinter as tk
import tkinter.ttk as widgets
import tkinter.messagebox as msg

# create app
root = tk.Tk()

# declare variable which will hold width and height user input
width_variable = tk.StringVar(value="1.2345")
height_variable = tk.StringVar(value="4.56789")


def calc_command():
    """Function is bound to click event of calculate button"""
    w = float(width_variable.get())
    h = float(height_variable.get())
    circumference = (w + h) * 2
    area = w * h
    msg.showinfo("Rectangle", f"a rectangle of {w:0.2f}x{h:0.2f} has \nan circumference of {circumference:0.2f} and an \narea of {area:0.2f}")


# set up root (main window)
root.title("Rectangle calculator")
root.geometry("200x85")
root.resizable(False, False)

root.columnconfigure(1, weight=1)

widgets.Label(root, text="Width:").grid(row=0, column=0, pady=3, padx=3)
widgets.Label(root, text="Height:").grid(row=1, column=0, pady=3, padx=3)

widgets.Entry(root, textvariable=width_variable).grid(
    row=0, column=1, sticky=tk.EW, pady=3, padx=3)

widgets.Entry(root, textvariable=height_variable).grid(
    row=1, column=1, sticky=tk.EW, pady=3, padx=3)

widgets.Button(root, text="Calculate", command=calc_command).grid(row=2, columnspan=2, pady=3)

root.mainloop()
