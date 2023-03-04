import psycopg2
from psycopg2.extras import RealDictCursor

def select_all(query):
    conn = psycopg2.connect("dbname=recipeapp")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def select_one(query, params):
    conn = psycopg2.connect("dbname=recipeapp")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, params)
    result = cur.fetchone()
    return result

def insert(query, params):
    conn = psycopg2.connect("dbname=recipeapp")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def write(query, params):
    db_connection = psycopg2.connect("dbname=recipeapp")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    db_cursor.execute(
        query,
        params
    )
    db_connection.commit()
    db_cursor.close()
    db_connection.close()