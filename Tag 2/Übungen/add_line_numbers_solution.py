#!/usr/bin/env python3
# coding: utf8

def transform(input_file_name, output_file_name):
    line_number = 1
    with open(input_file_name, 'r') as input_file:
        with open(output_file_name, 'w') as output_file:        
            while True: 
                line = input_file.readline() # don't strip the trailing newline
                if not line: break 
                
                line_number_str = f'{line_number:2}) '
                if len(line.strip()) == 0:
                    line_number_str = ''

                output_file.write(f'{line_number_str}{line}') # since newline is still here, no need to append another one
                line_number += 1


if __name__ == '__main__':
    transform('Data/2_test.txt', 'Data/.2_test_with_line_numbers.txt')