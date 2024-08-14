import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        user='root',
        password='password',
        host='db',
        port='3306',
        database='ling_classifier'
    )

    if connection.is_connected():
        print('Successfully connected to the database')
        cursor = connection.cursor()
        cursor.execute('SELECT DATABASE();')
        print('Database connected:', cursor.fetchone())

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        connection.close()
