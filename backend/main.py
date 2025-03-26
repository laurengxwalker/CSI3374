from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import psycopg2

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    rating: str

@app.get("/movies", response_model=List[Movie])

def get_movies(genre: str = None, rating: str = None):
    conn = psycopg2.connect(dbname="movies_db", user="user", password="password", host="db")
    cursor = conn.cursor()

    query = "SELECT * FROM movies WHERE (%s IS NULL OR genre = %s) AND (%s IS NULL OR rating = %s)"
    cursor.execute(query, (genre, genre, rating, rating))

    movies = cursor.fetchall()
    conn.close()

    return [{"id": movie[0], "title": movie[1], "genre": movie[2], "rating": movie[3]} for movie in movies]
