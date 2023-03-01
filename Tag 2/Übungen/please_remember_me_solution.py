#!/usr/bin/env python3
# coding: utf8

import os.path
import json
from datetime import datetime

def load_last_logins(json_file_name):
    result = dict()
    if os.path.exists(json_file_name):
        with open(json_file_name, 'r') as input_file:
            result = json.load(input_file)           
    return result

def main():
    json_file_name = "Übungen/.all_logins.json"
    all_logins = load_last_logins(json_file_name)

    user_name = input("Please enter you name: ")

    last_login = "<never>"
    current_time = datetime.now().strftime("%d. %b. %Y %H:%M:%S")


    # determine if user already logged in and if yes, fetch the date
    if user_name in all_logins:
        last_login = all_logins[user_name]

    print(f"Hello {user_name}\nyour last login was {last_login}.\nNow is {current_time}")

    # update and save the last_logins.json
    all_logins[user_name] = current_time
    with open(json_file_name, 'w') as output_file:
        json.dump(all_logins, output_file)




if __name__ == '__main__':
    main()