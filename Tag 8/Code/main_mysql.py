#!/usr/bin/env python3
# coding: utf8

import pymysql

def print_version(db_connection):
    """Prints the DATABAse type (MySQL) and the driver version."""

    cursor = db_connection.cursor()  
    cursor.execute('SELECT VERSION()')

    version = cursor.fetchone()[0]
    print(f'MySQL version {version}')

    cursor.close()

def main():
    db_connection = pymysql.connect(host='localhost', port=3307, user='python_user', passwd='eden2222', database='small_shop_demo')

    print_version(db_connection)
   
    cursor = db_connection.cursor()  

    cursor.execute('SELECT * FROM Customers LIMIT 10')

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    main()



