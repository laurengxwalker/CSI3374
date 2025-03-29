# Movie-Recommender (Docker Project CSI 3374)
Kailynn Savage, Lauren Walker, Tara Williams 

**Overview**
* Using open-source lists of movies, their genres, ratings, etc., the website will return movies based on inputted fields. Anyone can use the website, but it is specifically made for movie enthusiasts who seek to watch movies with certain criteria.The data this website will need will be taken from the many publicly available movie repositories that contains ratings of the movies such as IMDB. The data will be retrieved either from downloadable csv's from the website or through web-scrapingThe key features it will need are input fields where a user can choose from a dropdown list of genres and ratings to filter movies, and another page that returns all of the movies matching the criteria.


**Current Project**
* The current proejct has a frontend built with React, a backend built with FastAPI, and PostgreSQL database that has a small subset of movies. Docker is used to containerize the features. Docker-compose is used to build the application 

**For the Future**
The project would need more development for a working website, including a user interface. It would also need a connection to an API to have more updated data. This may result in changing the structure of the Postgre-SQL database. 

## Setup Instructions
*  Clone the repository and navigate to the project directory.
*  Make sure Docker and Docker Compose are installed.
*  Copy `.env.example` to `.env` and adjust the values as needed.


1. **Clone the repository**:
   ```bash
   git clone [https://github.com/username/project.git](https://github.com/laurengxwalker/CSI3374.git)
   cd CSI3374

2. **In terminal**:
   * To start the app:
         * run docker -compose up --build
         * The React app will be available at http://localhost:3000.
         * The FastAPI backend will be available at http://localhost:8000.
         * pgAdmin was not used. 
  
4. **To stop the application**:
   * Run docker compose down 
