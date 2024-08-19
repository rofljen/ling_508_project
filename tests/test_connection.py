import mysql.connector
import os
from os import environ
import pytest


def test_db_connection():
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_NAME')
    }

    # Validate configuration
    for key, value in config.items():
        if value is None:
            pytest.fail(f"Missing environment variable: {key}")

    try:
        # Ensure port is an integer
        if config['port'] is not None:
            config['port'] = int(config['port'])

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**config)

        # Create a cursor and execute a simple query
        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()

        # Close the connection
        cursor.close()
        connection.close()

        assert result is not None  # Ensure the query returned a result

    except Exception as e:
        pytest.fail(f"Database connection failed: {str(e)}")
