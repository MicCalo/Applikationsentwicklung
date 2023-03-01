#!/usr/bin/env python3
# coding: utf8

# Integer
my_int = 42
print(f"my_int is of type {type(my_int)} and value is {my_int}") # Output: my_int is of type <class 'int'> and value is 42

# float
my_float = 23.5
print(f"my_float is of type {type(my_float)} and value is {my_float}") # Output: my_float is of type <class 'float'> and value is 23.5

# boolean
my_bool = True # or False
print(f"my_float is of type {type(my_bool)} and value is {my_bool}") # Output: my_float is of type <class 'bool'> and value is True

# strings
my_str = "hello world"
print(f"my_str is of type {type(my_str)} and value is '{my_str}'") # Output: my_str is of type <class 'str'> and value is 'hello world'

# list
my_list = [my_int, my_float, my_bool, my_str, None]
print(f"my_list is of type {type(my_list)} and value is {my_list}") # Output: my_list is of type <class 'list'> and value is [42, 23.5, True, 'hello world', None]

# dictionary
my_dict = {'my_int': my_int, 'my_float': my_float, 'my_str': my_str}
print(f"my_dict is of type {type(my_dict)} and value is {my_dict}") # Output: my_dict is of type <class 'dict'> and value is {'my_int': 42, 'my_float': 23.5, 'my_str': 'hello world'}

# tuple
my_tuple = (my_int, my_float, my_bool, my_str, None)
print(f"my_tuple is of type {type(my_tuple)} and value is {my_tuple}") # Output: my_tuple is of type <class 'tuple'> and value is (42, 23.5, True, 'hello world', None)