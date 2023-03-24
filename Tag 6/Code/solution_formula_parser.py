#!/usr/bin/env python3
# coding: utf8

class ParserException(Exception):
    """Custom Exception which is thrown/raised when parsing fails."""
    pass


def parse_number(input_string: str)-> int | float:
    """Tries to parse a string either as integer or as float value. If this fails, this function raises a ParserException."""
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError:
            raise ParserException(f"'{input_string}' is not a number")
        

def parse_expression(input_string: str) -> tuple:
    """Tries to parse a simple expression of the form '3 + 4' - three tokens separated by spaces. If input_string does not consist of three tokens or if first and last token is nut a number, , a ParserException is thrown."""
    tokens = input_string.split(' ')
    if len(tokens) != 3:
        raise ParserException(f"Three tokens expected but got {len(tokens) }")
    
    a = parse_number(tokens[0]) 
    op = tokens[1]
    b = parse_number(tokens[2])
    return (a, op, b)

def evaluate_expression(expression: tuple) -> int | float:
    """Evaluates a tuple of the form (number, operation, number) where op must be in [+-/*]. If string is not a simple operator, a ParserException is thrown."""
    if len(expression) != 3:
        raise ValueError("Tuple with 3 tokens expected")
    a = expression[0]
    op = expression[1]
    b = expression[2]
    if op == '+':
        return a  + b
    elif op == '-':
        return a - b   
    elif op == '*':
        return a * b   
    elif op == '/':
        return a / b
    else:
        raise ParserException(f"Operator '{op}' is not recognized")
    
def main():
    while True:
        input_string = input(">>> ")
        try:
            expression = parse_expression(input_string)
            result = evaluate_expression(expression)
            print(f"{input_string} = {result}")

            # print types of operands and of result
            print(f"'{expression[0]}' is {type(expression[0])}")
            print(f"'{expression[2]}' is {type(expression[2])}")
            print(f"result is {type(result)}")
        except ParserException as ex:
            print(f"Error while parsing '{input_string}': {ex}")

if __name__ == '__main__':
    main()

class MyException(Exception) : 
	pass

def foo_bar():
	raise MyException()

try:
	foo_bar()
except MyException as ex:
	print(f"The expected occurred: {ex}")