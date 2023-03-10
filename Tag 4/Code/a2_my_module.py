#!/usr/bin/env python3
# coding: utf8

"""This is a simple module, consisting of a single file to demonstrate import of variables, functions and classes."""

the_answer = 42
""""answer of the ultimate Question of Life, the Universe, and Everything"""

def my_adding_function(a: int, b: int) -> int:
    """Adds two integers """
    return a + b

class MyClass:
    """very simple class whose instances only have a name and almost no functionality."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"an instance of MyClass with name '{self.name}'"


print(f"imported {__name__}")

if __name__ == '__main':
    test = MyClass('hallo')
    print(test)

