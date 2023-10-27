# TODO: Feature 4
import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_id_found():
    repo = get_movie_repository()
    repo.clear_db()  
    known_movie = repo.create_movie("Inception", "Christopher Nolan", 9)

    result = repo.get_movie_by_id(known_movie.movie_id)

    assert result is not None
    assert isinstance(result, Movie)
    assert result.movie_id == known_movie.movie_id
    assert result.title == "Inception"

def test_get_movie_by_id_not_found():
    repo = get_movie_repository()
    repo.clear_db() 
    some_random_id = 9999999
    
    result = repo.get_movie_by_id(some_random_id)
    
    assert result is None
