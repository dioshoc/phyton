from psycopg2 import Error

from todos import print_error, close_connection, connection, cursor


def delete_data(remove_id):
    try:
        sql_delete_query = """Delete from todo where ID = %s"""
        cursor.execute(sql_delete_query, (remove_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно удалена")

    except (Exception, Error) as error:
        print_error(error)
    finally:
        if connection: close_connection()
