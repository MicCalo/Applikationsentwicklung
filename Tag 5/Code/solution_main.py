#!/usr/bin/env python3
# coding: utf8
import sys

from solution_date_functions import *
from solution_os_functions import *
from solution_platform_functions import *
from solution_requests_functions import *

instructions = """Following commands are available:

Remarks:
Dates have to be inserted in YYYY-MM-DD format

 1 - ask for an amount of days and calculate and print the date from now (now + days)
 2 - ask for an amount of days and calculate and print when that date was (now - days)
 3 - ask for a date and an amount of days to calculate and print a second date (date + days)
 4 - ask for two dates and calculate and print the time delta in days (date2 - date1)

10 - print current directory
11 - print items of current directory ('ls'/'dir')
12 - move one directory up ('cd ..')
13 - ask for a sub-directory name and go into ('cd xyz')

30 - print computer name
31 - print operating system
32 - print platform info
33 - print Python version

40 - download and print a web page

 ? - print this instructions again
 e - exit program\n"""

def main():
    print(sys.argv)
    
    terminate = False
    print(instructions)

    while not terminate:

        cmd = input("command: ")

        if cmd == '1':
            add_days_to_now()
        elif cmd == '2':
            subtract_days_from_now()
        elif cmd == '3':
            add_days_to_date()
        elif cmd == '4':
            get_time_delta()
        elif cmd == '10':
            print_cwd()
        elif cmd == '11':
            list_dir()
        elif cmd == '12':
            chg_dir_up()
        elif cmd == '13':
            chg_dir_down()
        elif cmd == '30':
            print_computer_name()
        elif cmd == '31':
            print_os()
        elif cmd == '32':
            print_platform_info()
        elif cmd == '33':
            print_python_version()
        elif cmd == '40':
            download_web_page()
        elif cmd == '?':
            print(instructions)
        elif cmd == 'e':
            terminate = True
        else:
            print(f"command {cmd} not recognized")


if __name__ == '__main__':
    main()

