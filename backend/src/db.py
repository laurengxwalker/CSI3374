import psycopg2
from psycopg2 import sql

def get_db_connection():
    try:
        # Establish the database connection
        conn = psycopg2.connect(
            dbname="movie_db", 
            user="user",       
            password="password",  
            host="postgres",     
            port="5432"           
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None
