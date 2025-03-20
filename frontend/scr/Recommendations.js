import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ResultsPage = ({ filters }) => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    if (filters.genre || filters.rating) {
      axios.get('http://localhost:8000/movies', {
        params: { genre: filters.genre, rating: filters.rating }
      })
      .then(response => setMovies(response.data))
      .catch(error => console.error(error));
    }
  }, [filters]);

  return (
    <div>
      <h1>Recommended Movies</h1>
      <ul>
        {movies.map(movie => (
          <li key={movie.id}>{movie.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default ResultsPage;
