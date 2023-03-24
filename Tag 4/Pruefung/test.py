#!/usr/bin/env python3
# coding: utf8

#Count all lines
with open('Pruefung/sample-2mb-text-file.txt', 'r') as f:
    lines = len(f.readlines())
print(lines)

#Count lines if "est" is included
file = open('Pruefung/sample-2mb-text-file.txt','r')
keyword = 'est'
count = 0
for line in file:
    if keyword in line:
        count = count + 1
print(count)