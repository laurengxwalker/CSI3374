import React, { useState } from 'react';

const MovieFilter = ({ onFilterSubmit }) => {
  const [genre, setGenre] = useState('');
  const [rating, setRating] = useState('');

  const handleSubmit = () => {
    onFilterSubmit({ genre, rating });
  };

  return (
    <div>
      <select onChange={(e) => setGenre(e.target.value)}>
        <option value="">Select Genre</option>
        <option value="Action">Action</option>
        <option value="Drama">Drama</option>
        <option value="Comedy">Comedy</option>
        <option value="Romance">Romance</option>
      </select>
      
      <select onChange={(e) => setRating(e.target.value)}>
        <option value="">Select Rating</option>
        <option value="G">G</option>
        <option value="PG">PG</option>
        <option value="PG-13">PG-13</option>
        <option value="R">R</option>
      </select>
      
      <button onClick={handleSubmit}>Filter Movies</button>
    </div>
  );
};

export default MovieFilter;
