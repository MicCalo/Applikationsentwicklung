#!/usr/bin/env python3
# coding: utf8

import os.path
from datetime import datetime

def load_last_logins(json_file_name):
    result = dict()
    if os.path.exists(json_file_name):
        # TODO: load the json
        pass
    return result

def main():
    json_file_name = "Übungen/.all_logins.json"
    all_logins = load_last_logins(json_file_name)

    user_name = input("Please enter you name: ")

    last_login = "<never>"
    current_time = datetime.now().strftime("%d. %b. %Y %H:%M:%S")


    # TODO: determine if user already logged in and if yes, fetch the date
    # ...

    print(f"Hello {user_name}\nyour last login was {last_login}.\nNow is {current_time}")

    # TODO: update and save the last_logins.json
    # ...


if __name__ == '__main__':
    main()