#!/usr/bin/env python3
# coding: utf8

def demo1():
    input_file = open('test.txt', 'r')
    while True: 
        line = input_file.readline()
        if not line: break 
        print(line.rstrip())

def demo_catch_all():
    try:
        input_file = open('test.txt', 'r')
        while True: 
            line = input_file.readline()
            if not line: break 
            print(line.rstrip())

    except: # catch all exceptions
        print(f"reading file failed")

def demo_finally(value):
    try:
        print("open resource")
        print(f"Do something: {int(value)}")
        return
        print("dead code here")
    except ValueError:
        print("ValueError occurred")
    finally:
        print("close resource")
       

def demo_finally_real():
    try:
        input_file = open('test.txt', 'r')
        while True: 
            line = input_file.readline()
            if not line: break 
            print(line.rstrip())
        return

    except IOError as ioError:
        print(f"reading file failed: {ioError}")
    
    finally:
        if 'input_file' in locals() and input_file:
            input_file.close()

def my_function(number):
    if not isinstance(number, int):
        raise TypeError("'number' must be a int")
    if number < 0:
        raise ValueError("'number' must be positive")
    return number + 1

if __name__ == '__main__':
    demo_finally("hallo")
    
    print(my_function(1))   
    print(my_function("foo bar")) 
    print(my_function(-42))