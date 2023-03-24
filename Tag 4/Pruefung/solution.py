#!/usr/bin/env python3
# coding: utf8

import os

print(f"cwd:   {os.getcwd()}")
print(f"Files: {os.listdir()}")

with open('sample-2mb-text-file.txt', 'r') as f:
    lines_total = 0
    lines_with_est = 0
    while True:
        line = f.readline()
        if line:
            lines_total+=1
            if 'est' in line:
                lines_with_est += 1
        else: break

print(f"lines total:      {lines_total}")
print(f"lines with 'est': {lines_with_est}")