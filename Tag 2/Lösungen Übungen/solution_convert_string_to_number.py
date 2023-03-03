#!/usr/bin/env python3
# coding: utf8

"""
Codewars Kata 'Convert a String to a Number!'

see https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
"""

import codewars_test as test

def string_to_number(s):
    return int(s)

@test.describe("string_to_number")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_to_number("1234"), 1234)
        test.assert_equals(string_to_number("605"), 605)
        test.assert_equals(string_to_number("1405"), 1405)
        test.assert_equals(string_to_number("-7"), -7)