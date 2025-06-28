#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def main():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='mysqluser',
            password='password!'
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as err:
        print(f"Error while connecting to MySQL: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
