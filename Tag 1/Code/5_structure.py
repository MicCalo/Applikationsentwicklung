#!/usr/bin/env python3
# coding: utf8

# define a function without parameter
def function_if_demo():
    """ function with an if in it """
    list = range(10)
    for i in list:  # range(10) -> list -> [0, 1, 2, ...., 9]
        is_even = (i % 2) == 0
        if is_even:
            print(f"{i} is even")
        else:
             print(f"{i} is odd")

#define a function with one parameter             
def function_loop_demo(my_dict):
    """function to demonstrate for-loops"""

    print("for-loop iterating over values 1, 2 and 3")
    for key in range(1, 4):
       print(f"{key}: {my_dict[key]}")


    print("\n\nfor-loop iterating over all keys in a dict")
    pos = 1
    for key in my_dict.keys():
       print(f"#{pos} - {key}: {my_dict[key]}")
       pos = pos + 1



    print("\n\nfor-loop over all key/value tuples (unpacked) in a dict [advanced]")
    for key, value in my_dict.items(): # items delivers an iterable of tuples. By stating the correct amount of variable names, the tuple gets unpacked
        print(f"#{key}: {value}")

def main():
    function_if_demo()
    demo_dict = {'key1': "first entry", 'key2': "second entry", "answer": 42, 3: "trois", 2: "deux", 1: "un" }
    function_loop_demo(demo_dict)

# this if makes sure that if the file is used as a library, the functions are not invoked
if __name__ == '__main__':
    main()
