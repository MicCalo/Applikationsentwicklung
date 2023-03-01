#!/usr/bin/env python3
# coding: utf8

"""
Codewars Kata 'Convert a Boolean to a String'

see https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
"""
import codewars_test as test

def boolean_to_string(b):
    if b:
        return "True"
    else:
        return "False"

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")