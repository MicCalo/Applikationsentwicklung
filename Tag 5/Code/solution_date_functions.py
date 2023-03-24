#!/usr/bin/env python3
# coding: utf8

import datetime

def add_days_to_now():
    days = int(input("days: "))
    now = datetime.date.today()
    date = now + datetime.timedelta(days)
    print(f"today ({now.strftime('%d. %b %Y')}) plus {days} days is {date.strftime('%d. %b %Y')}")

def subtract_days_from_now():
    days = int(input("days: "))
    now = datetime.date.today()
    date = now - datetime.timedelta(days)
    print(f"today ({now.strftime('%d. %b %Y')}) minus {days} days was {date.strftime('%d. %b %Y')}")

def add_days_to_date():
    date = datetime.date.fromisoformat(input("date: "))
    days = int(input("days: "))
    end_date = date + datetime.timedelta(days)
    print(f"{date.strftime('%d. %b %Y')} plus {days} days = {end_date.strftime('%d. %b %Y')}")

def get_time_delta():
    date1 = datetime.date.fromisoformat(input("first: "))
    date2 = datetime.date.fromisoformat(input("second: "))
    delta = date2 - date1
    print(f"Between {date1.strftime('%d. %b %Y')} and {date2.strftime('%d. %b %Y')} are {delta.days} days")


