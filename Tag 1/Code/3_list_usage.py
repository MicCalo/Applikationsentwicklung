#!/usr/bin/env python3
# coding: utf8

list = []

list.append("first entry")
list.append("second entry")
list.append(range(3)) # append adds one entry, here a Range
list.extend(range(3)) # append adds multiple entries, here a Range
list.extend('abc') # append adds multiple entries, here 'a', 'b' and 'c'
list.insert(2, "third entry") # inserts an entry at a certain position

print(f"list = {list}") # Output: list = ['first entry', 'second entry', 'third entry', range(0, 3), 0, 1, 2, 'a', 'b', 'c']

print(f"index of element 'third entry': {list.index('third entry')}") # Output: index of element 'third entry': 2

del list[3] # deletes the 4th entry (-> zero based), here the Range object
del list[3:5] #deletes the 4th and the 5th entry, here 0 and 1
print(f"list = {list}") # Output: list = ['first entry', 'second entry', 'third entry', 0, 1, 2]
print(f"len(list) = {len(list)}") # Output: len(list) = 7


list.clear()

print(f"len(list) = {len(list)}") # Output: len(list) = 0

