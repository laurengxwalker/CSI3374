import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MovieFilter from './components/MovieFilter';
import ResultsPage from './pages/ResultsPage';

const App = () => {
  const [filters, setFilters] = useState({ genre: '', rating: '' });

  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <MovieFilter onFilterSubmit={setFilters} />
        </Route>
        <Route path="/results" exact>
          <ResultsPage filters={filters} />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;