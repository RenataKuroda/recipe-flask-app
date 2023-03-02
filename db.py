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