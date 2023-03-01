#!/usr/bin/env python3
# coding: utf8

import json

# 1) Read JSON file 'the_gang.json' and return the data
def read_json(file_name='Übungen/the_gang.json'):
    """Read a JSON file."""
    data = None
    with open(file_name, 'r') as input_file:
        data = json.load(input_file)

    return data


# 2) function to calculate the average age
def calculate_age_average(people_dict):
    """Function to calculate the average age. people_dict is expected to be a dictionary with sub-dictionaries which contains 'Age'."""
    sum = 0.0
    for  person in people_dict.values():
        age = float(person['Age'])  # fetch Age of that person
        sum += age                  # sum up Age

    return sum / len(people_dict)

# 3) Function to collect the hair colors and their amounts
def get_hair_colors(people_dict):
    """Function to accumulate hair colors and the occurrences. people_dict is expected to be a dictionary with sub-dictionaries which contains 'Hair'."""
    result = dict()
    for person in people_dict.values():
        hair_color = person['Hair']                       # fetch hair color
        
        if hair_color in result:                          # if hair color is already 'registered'...
            result[hair_color] = result[hair_color] +  1  # ... then increment its counter by 1
        else:            
            result[hair_color] = 1                        # otherwise, start its counter

    return result


def main():
    the_gang = read_json()

    # Call the functions on the_gang
    avg_age = calculate_age_average(the_gang)
    hair_colors = get_hair_colors(the_gang)

    # 4) Print those values and the number of gang members
    print(f"avg. age: {avg_age:.1f}")
    print(f"hair colors: {hair_colors}")
    print(f"count: {len(the_gang)}")

    # 5) Save the results in another JSON File
    results = {
        'avg_age': avg_age,
        'hair_colors': hair_colors,
        'count': len(the_gang)
    }

    with open('Übungen/.results_the_gang.json', 'w') as output_file:
        json.dump(results, output_file, indent=4)


if __name__ == '__main__':
    main()
