import psycopg2
from config import *
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    # Connecting to an existing database
    connection = psycopg2.connect(
                                    user=user,
                                    password=password,
                                    host=host,
                                    port=port
                                    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Cursor to perform operations with the database
    with connection.cursor as cursor:
        sql_create_database = 'create database postgres_db'
        cursor.execute(sql_create_database)

except (Exception, Error) as error:
    print("Error when working with PostgreSQL", error)

finally:
    if connection:
        connection.close()
        print("Connection to PostgreSQL is closed")