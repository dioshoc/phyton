from psycopg2 import Error

from todos import print_error, close_connection, connection, cursor


def update_data(update_id, title, description, complete):
    try:
        sql_select_query = """select * from todo where id = %s"""
        cursor.execute(sql_select_query, update_id)
        record = cursor.fetchone()

        new_object = (
            title or record[1],
            description or record[2],
            complete or record[3],
            update_id
        )

        sql_update_query = """
        Update todo set 
        title       = %s, 
        description = %s, 
        complete    = %s 
        where id    = %s
        """

        cursor.execute(sql_update_query, new_object)
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно обновлена")

    except (Exception, Error) as error:
        print_error(error)
    finally:
        if connection: close_connection()
