#!/usr/bin/env python3
# coding: utf8

def read_csv(file_name):
    cells = []
    with open(file_name, 'r') as input_file:
        while True: 
            line = input_file.readline().strip()
            if not line: break 
            cells.append(line.split(';')) # append the tokens as a new list 

    # return cells # plain list of lists

    as_dicts = []
    for i in range(1, len(cells)): # from row 1 (second) to and including last row
        row_data = dict()
        as_dicts.append(row_data)
        for j in range(len(cells[0])):
            row_data[cells[0][j]] = cells[i][j]
    return as_dicts


if __name__ == '__main__':
    data = read_csv('Übungen/test.csv')
    print(data)