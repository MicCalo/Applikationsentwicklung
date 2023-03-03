#!/usr/bin/env python3
# coding: utf8

"""
Codewars Kata 'Pythagorean Triple'

see https://www.codewars.com/kata/5951d30ce99cf2467e000013/train/python
"""

import codewars_test as test

def sqr(x):
    return x * x

def pythagorean_triple(integers):
    result = False    
    if len(integers) == 3:
        a, b, c = sorted(integers)
        result = sqr(a) + sqr(b) == sqr(c)
    return result 

test.assert_equals(pythagorean_triple([3, 4, 5]), True)
test.assert_equals(pythagorean_triple([3, 5, 9]), False)
