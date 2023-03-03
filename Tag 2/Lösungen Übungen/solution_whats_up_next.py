#!/usr/bin/env python3
# coding: utf8

"""
Codewars Kata 'What's up next?'

see https://www.codewars.com/kata/542ebbdb494db239f8000046/train/python
"""

import codewars_test as test

def next_item(xs, item):
    """ 'good enough' solution, won't pass the last test case."""
    if item in xs:
        index = xs.index(item)
        if index < len(xs) - 1:
            return xs[index + 1]
    return None

def next_item_improved(xs, item):
    result = None
    if xs: 
        i = iter(xs)   
        for x in i:
            if x == item:
                break  
        if i:
            try:
                result = next(i)
            except StopIteration:
                result = None
    return result

@test.describe('next_item')
def test_next_item():
    @test.it('should pass some tests')
    def tests():
        test.assert_equals(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)
        test.assert_equals(next_item(['a', 'b', 'c'], 'd'), None)
        test.assert_equals(next_item(['a', 'b', 'c'], 'c'), None) 
        test.assert_equals(next_item(None, 'c'), None)
        test.assert_equals(next_item('testing', 't'), 'e')
        test.assert_equals(next_item(iter(range(1, 30000)), 12), 13)
