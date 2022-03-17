# TODO: Feature 2
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_create_movie():
    movie = MovieRepository.create_movie("It Follows","David Robert Mitchell",6.8)
    assert movie.title == "It Follows"