
import mysql.connector
from mysql.connector import Error

def main():
    connection = None
    cursor = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='mysqluser',          # or any user with CREATE DATABASE privilege
            password='password!'
        )
        cursor = connection.cursor()
        # Create the alx_book_store database if it does not already exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        # Handle any errors that occur during connection or execution
        print(f"Error while connecting to MySQL: {err}")
    finally:
        # Clean up cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
