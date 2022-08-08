from psycopg2 import Error
from todos import print_error, close_connection, connection, cursor


def add_data(add_id, title, description, complete=False):
    try:
        postgres_insert_query = """ 
        INSERT INTO todo (ID, TITLE, DESCRIPTION, COMPLETE)
        VALUES (%s,%s,%s,%s)"""
        new_data = (add_id, title, description, complete)
        cursor.execute(postgres_insert_query, new_data)
        connection.commit()

        count = cursor.rowcount
        print(count, "Запись успешно добавлена в таблицу todo")

    except (Exception, Error) as error:
        print_error(error)
    finally:
        if connection: close_connection()
