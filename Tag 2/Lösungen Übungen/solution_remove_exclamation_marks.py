#!/usr/bin/env python3
# coding: utf8

"""
Codewars Kata ' Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string'

see https://www.codewars.com/kata/57faf12b21c84b5ba30001b0/train/python
"""

import codewars_test as test

def remove(s):
    return f"{s.replace('!', '')}!"


test.describe("Basic Tests")

tests = [
    ["Hi!" , "Hi!"],
    ["Hi!!!" ,"Hi!"],
    ["!Hi" , "Hi!"],
    ["!Hi!" , "Hi!"],
    ["Hi! Hi!" , "Hi Hi!"],
    ["Hi" , "Hi!"],
]

for inp, exp in tests:
    test.assert_equals(remove(inp), exp)