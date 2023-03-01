#!/usr/bin/env python3
# coding: utf8

"""
Codewars Kata 'Count of positives / sum of negatives'

see https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
"""
import codewars_test as test

def count_positives_sum_negatives(arr):
    """ 
    straight-forward implementation with a for-loop, an if and successive summing up/counting.
    """
    if not arr:
        return []

    count_positives = 0
    sum_negatives = 0
    for x in arr:
        if x>0:
            count_positives += 1
        else:
            sum_negatives += x
   
    return [count_positives, sum_negatives]



@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
        test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
        test.assert_equals(count_positives_sum_negatives([1]),[1,0])
        test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
        test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
        test.assert_equals(count_positives_sum_negatives([]),[])