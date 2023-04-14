#!/usr/bin/env python3
# coding: utf8

import sqlite3

def print_version(db_connection):
    """Prints the database type (SQLite) and the driver version."""
    cursor = db_connection.cursor()  
    cursor.execute('SELECT sqlite_version()')

    version = cursor.fetchone()[0]
    print(f'SQLite version {version}')

    cursor.close()

def main():
    # open database - if it does not exist, it will be created so this seldom fails
    db_connection = sqlite3.connect('small_shop_demo.db')

    # SQLite does not enforce foreign key constraints by default so turn this on.
    db_connection.cursor().execute('PRAGMA foreign_keys = ON')

    print_version(db_connection)

    cursor = db_connection.cursor()

    cursor.execute('SELECT * FROM Customers LIMIT 10')

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    main()



