import psycopg2
from psycopg2 import Error


def print_error(error):
    print("Ошибка при работе с PostgreSQL", error)


def close_connection():
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")


try:
    connection = psycopg2.connect(
        database='postgres',
        user='loh',
        password='sam_takoi',
        host='localhost',
        port="5432"
    )
    cursor = connection.cursor()
except (Exception, Error) as error:
    print_error(error)
