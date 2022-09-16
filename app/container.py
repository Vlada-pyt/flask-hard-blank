from app.dao.directors import DirectorDAO
from app.dao.genres import GenreDAO
from app.dao.movies import MovieDAO
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService
from setup_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)