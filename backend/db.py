import psycopg2
from psycopg2 import sql

def get_db_connection():
    conn = psycopg2.connect(
        dbname="movies_db", user="user", password="password", host="db"
    )
    return conn