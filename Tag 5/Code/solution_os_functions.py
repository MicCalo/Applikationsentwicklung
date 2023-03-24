#!/usr/bin/env python3
# coding: utf8

import os

def print_cwd():
    print(f"current path: {os.getcwd()}")

def list_dir():
    file_items = os.listdir(os.getcwd())
    print(f"{len(file_items)} items in {os.getcwd()}:")
    print("  "+"\n  ".join(file_items))

def chg_dir_up():
    os.chdir('../')

def chg_dir_down():
    sub_dir = input('dir: ')
    file_items = os.listdir(os.getcwd())
    if sub_dir in file_items:
        os.chdir(sub_dir)
    else:
        print("invalid sub directory")
