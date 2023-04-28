# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets


class FrameBase(widgets.Frame):
    """base class for one notebook frame (aka tab item). They extend the Frame from TK widgets and add a caption."""
    show_frame_borders = False

    def __init__(self, container, caption: str):
        widgets.Frame.__init__(self, container)
        self.caption = caption
        self.setup()
        self.borderize(self, tk.RAISED)
        self.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

    def setup(self):
        """Virtual method to setup the main frame. Should add and configure all required children"""
        pass

    def borderize(self, frame: widgets.Frame, kind: str = tk.SOLID):
        """ Adds border to the frame if static field FrameBase.show_frame_borders is true. This is helpful to see the frames during development."""
        if FrameBase.show_frame_borders:
            frame['borderwidth'] = 2
            frame['relief'] = kind
