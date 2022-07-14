import sys
import psycopg2
import os
import pandas as pd
import psycopg2.extras as extras


def _execute_values(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")

    query = "SELECT setval(pg_get_serial_sequence('%s', 'id'), (SELECT MAX(id) FROM %s)+1)" % (table, table)

    cursor.execute(query)
    conn.commit()
    cursor.close()


def _load(conn, name: str):
    file_path = f"./data/{name}.json"
    df = pd.read_json(file_path).fillna('')
    df.drop(labels=['id'], axis=1)
    _execute_values(conn=conn, df=df, table=name)


def _connect(params_dic):
    try:
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Connection ERROR...")
        print(error)
        sys.exit(1)
    print("Connection successful")

    return connection


if __name__ == "__main__":
    param_dic = {
        "host": os.getenv("POSTGRES_SERVER"),
        "database": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD")
    }

    conn = _connect(param_dic)

    _load(conn, "organizations")
    _load(conn, "bikes")
