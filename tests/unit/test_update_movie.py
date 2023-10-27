# TODO: Feature 5 unit test
import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_update_movie_pass():
    movie = get_movie_repository()
    movie.clear_db()
    movie.create_movie('Inception', 'Chrostoper Nolan', 5)
    movie.create_movie('Interstellar', 'Chrostoper Nolan', 5)
    movie.create_movie('Jurassic Park', 'Steven Spielberg', 5)
    movie_to_be_edited = movie.get_movie_by_title('Inception')
    movie_to_be_edited = movie.update_movie('Justice League', 'Zack Snyder', 2)
    

def test_update_movie_fail():
    movie = get_movie_repository()