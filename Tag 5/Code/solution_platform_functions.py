#!/usr/bin/env python3
# coding: utf8

import platform

def print_computer_name():
    print(f"computer name: {platform.node()}")
    
def print_os():
    print(f"OS name: {platform.system()}")
    
def print_platform_info():
    print(f"platform info: {platform.platform()}")
    
def print_python_version():
    print(f"python version: {platform.python_version()}")