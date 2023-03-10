#!/usr/bin/env python3
# coding: utf8

print("test")

import a2_my_module

print("a2_my_module.__doc__:")
print(a2_my_module.__doc__)
print()

print(f"a2_my_module.the_answer:               {a2_my_module.the_answer}")
print(f"a2_my_module.my_adding_function:       {a2_my_module.my_adding_function}") # function is just stated, not invoked...
print(f"a2_my_module.my_adding_function(1, 1): {a2_my_module.my_adding_function(1, 1)}")


test = a2_my_module.MyClass("test")
print(f"test:                                  {test}")

# for classes, approach above ist not very convenient. Usually, the dedicated single import is used
from a2_my_module import MyClass # usually, all imports are stated at the beginning of a file.    
test2 = MyClass("test2")
print(f"test2:                                 {test2}")


