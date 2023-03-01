#!/usr/bin/env python3
# coding: utf8

empty_dict = dict()
empty_dict['key1'] = "first entry"

my_dict = {'key1': "first entry", 'key2': "second entry"}
print(my_dict)
print(f"my_dict['key1'] = {my_dict['key1']}") # Output: my_dict['key1'] = first entry

print(f"len(my_dict) = {len(my_dict)}") # Output: len(my_dict) = 2


my_dict['key3'] = "third entry" # adding a new entry
my_dict['key3'] = "better third entry" # changing a new entry
print(f"my_dict['key3'] = {my_dict['key3']}") #output: my_dict['key3'] = better third entry