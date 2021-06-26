import os
import psycopg2
import psycopg2.extras as ext
import db_credentials as creds


def run_sql(sql, values=None):
    conn = None
    result_list = list()

    try:
        conn = psycopg2.connect(f'host={creds.HOST} port={creds.PORT} dbname={creds.DBNAME} user={creds.USER} password={creds.PASSWORD}')

        cursor = conn.cursor(cursor_factory=ext.DictCursor)
        cursor.execute(sql, values)

        conn.commit()
        result_list = cursor.fetchall()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return result_list
