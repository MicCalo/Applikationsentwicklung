# coding: utf8

import tkinter as tk
import tkinter.ttk as widgets

import webbrowser
import datetime

from b2_frame_base import FrameBase


class DateTimeFrame(FrameBase):

    def __init__(self, container,):
        FrameBase.__init__(self, container, "Date/Time")

    def setup(self):
        primary_frame = widgets.Frame(self)
        self.borderize(primary_frame, tk.GROOVE)
        primary_frame.pack(fill=tk.X)

        self.create_format_frame(primary_frame)
        self.current_datetime_frame = self.create_current_datetime_frame(
            primary_frame)

        primary_frame.pack(padx=10, pady=10)

        self.update_current()

    def show_cheat_sheet(self):
        webbrowser.open_new_tab('https://strftime.org/')

    def update_current(self):
        # fetch the format strings
        date_format_string = self.date_format_value.get()
        time_format_string = self.time_format_value.get()
        datetime_format_string = self.time_format_value.get()+' ' + \
            self.date_format_value.get()

        # update the values, using the format strings
        now = datetime.datetime.now()
        self.current_datetime_frame.children['$date']['text'] = now.date().strftime(
            date_format_string)
        self.current_datetime_frame.children['$time']['text'] = now.time().strftime(
            time_format_string)
        self.current_datetime_frame.children['$dateTime']['text'] = now.strftime(
            datetime_format_string)

    def create_format_frame(self, parent):
        # create string variables for the format specifier string
        self.date_format_value = tk.StringVar(value='%a, %d. %b %Y')
        self.time_format_value = tk.StringVar(value='%H:%M:%S')

        # create Frame and configure it to be a 3x2 grid
        format_frame = widgets.Frame(parent)

        format_frame.columnconfigure(0, minsize=120)
        format_frame.columnconfigure(1, weight=1)
        format_frame.columnconfigure(2, weight=1)
        format_frame.columnconfigure(3, minsize=80)
        format_frame.rowconfigure(0, weight=1)
        format_frame.rowconfigure(1, weight=1)

        # add labels and text input fields
        widgets.Label(format_frame, text="Format:").grid(
            column=0, row=1, sticky=tk.W)
        widgets.Label(format_frame, text="Date").grid(
            column=1, row=0, sticky=tk.W)
        widgets.Label(format_frame, text="Time").grid(
            column=2, row=0, sticky=tk.W)
        widgets.Entry(format_frame, textvariable=self.date_format_value).grid(
            column=1, row=1, sticky=tk.EW)
        widgets.Entry(format_frame, textvariable=self.time_format_value).grid(
            column=2, row=1, sticky=tk.EW)
        widgets.Button(format_frame, text="cheat sheet",
                       command=self.show_cheat_sheet).grid(column=3, row=1)

        self.borderize(format_frame)
        format_frame.pack(fill=tk.X, pady=3, padx=3)
        return format_frame

    def create_current_datetime_frame(self, parent):

        # create frame and configure it to be a 3x3 grid
        frame = widgets.Frame(parent)

        frame.columnconfigure(0, minsize=120)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, minsize=80)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        # add labels
        widgets.Label(frame, text="Current date:").grid(
            column=0, row=0, sticky=tk.W)
        widgets.Label(frame, text="Current time:").grid(
            column=0, row=1, sticky=tk.W)
        widgets.Label(
            frame, text="Current date/time:").grid(column=0, row=2, sticky=tk.W)

        widgets.Label(frame, name='$date', background='lightgray').grid(column=1, row=0, sticky=tk.EW)
        widgets.Label(frame, name='$time', background='lightgray').grid(column=1, row=1, sticky=tk.EW)
        widgets.Label(frame, name='$dateTime', background='lightgray').grid(column=1, row=2, sticky=tk.EW)

        widgets.Button(frame, text="update", command=self.update_current).grid(column=2, row=1)

        self.borderize(frame)
        frame.pack(fill=tk.X, pady=3, padx=3)

        return frame
