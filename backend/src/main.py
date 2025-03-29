from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.db import get_db_connection

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    rating: str

@app.get("/movies", response_model=List[Movie])

def get_movies(genre: str = None, rating: str = None):
    try:
        query = """
            SELECT * FROM movies
            WHERE (%s IS NULL OR genre = %s)
            AND (%s IS NULL OR rating = %s)
        """

        # Use the db connection context manager
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (genre, genre, rating, rating))
                movies = cursor.fetchall()

        # If no movies found, return an empty list
        if not movies:
            raise HTTPException(status_code=404, detail="Movies not found")

        # Prepare the result
        return [{"id": movie[0], "title": movie[1], "genre": movie[2], "rating": movie[3]} for movie in movies]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
