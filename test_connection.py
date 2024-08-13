import mysql.connector
import os

def test_connection():
    config = {
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'root'),
        'host': os.getenv('DB_HOST', 'db'),
        'port': os.getenv('DB_PORT', '3306'),
        'database': os.getenv('DB_NAME', 'ling_classifier')
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Successfully connected to the database")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    test_connection()
