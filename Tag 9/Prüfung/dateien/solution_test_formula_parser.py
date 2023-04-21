#!/usr/bin/env python3
# coding: utf8

from solution_formula_parser import parse_expression, evaluate_expression, ParserException

import unittest

class FormulaParserTest(unittest.TestCase):

    def test_parse_expression_int_when_possible(self):
        expression = parse_expression('1 + 2')
        
        self.assertEqual(len(expression), 3) 
        self.assertIsInstance(expression[0], int) 
        self.assertIsInstance(expression[2], int) 
        self.assertEqual(expression[0], 1)
        self.assertEqual(expression[1], '+')
        self.assertEqual(expression[2], 2)

    def test_parse_expression_float(self):
        expression = parse_expression('1.0 + 2.0')
        
        self.assertEqual(len(expression), 3) 
        self.assertIsInstance(expression[0], float) 
        self.assertIsInstance(expression[2], float) 
        self.assertEqual(expression[0], 1.0)
        self.assertEqual(expression[1], '+')
        self.assertEqual(expression[2], 2.0) 
        
    def test_parse_expression_mixed(self):
        expression = parse_expression('1 + 2.0')
        
        self.assertEqual(len(expression), 3) 
        self.assertIsInstance(expression[0], int) 
        self.assertIsInstance(expression[2], float) 
        self.assertEqual(expression[0], 1)
        self.assertEqual(expression[1], '+')
        self.assertEqual(expression[2], 2.0)

    def test_parse_throws_when_not_3_tokens(self):
        self.assertRaises(ParserException, parse_expression, "")
        self.assertRaises(ParserException, parse_expression, "1+2")
        self.assertRaises(ParserException, parse_expression, "a * 3")

    def test_evaluate_expression_returns_int_when_ints(self):
        result = evaluate_expression((3, '*', 4))

        self.assertIsInstance(result, int)
        self.assertEqual(result, 12)
        
    def test_evaluate_expression_returns_float_when_needed(self):
        result = evaluate_expression((3.0, '*', 4))

        self.assertIsInstance(result, float)
        self.assertEqual(result, 12.0)

    def test_evaluate_expression_throws_when_invalid_operator(self):
        self.assertRaises(ParserException, evaluate_expression, (3, '%', 4))

    def test_evaluate_expression_throws_when_invalid_tuple_too_long(self):
        self.assertRaises(ValueError, evaluate_expression, (3, '%', 4, '!'))

    def test_evaluate_expression_throws_when_invalid_tuple_too_short(self):
        self.assertRaises(ValueError, evaluate_expression, (3,  4))

if __name__ == '__main__':
    unittest.main()