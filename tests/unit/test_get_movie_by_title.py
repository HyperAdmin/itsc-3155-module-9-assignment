import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_title_found():
    repo = get_movie_repository()
    repo.clear_db()
    known_movie = repo.create_movie("Inception", "Christopher Nolan", 9)
    
    result = repo.get_movie_by_title("Inception")
    
    assert result is not None
    assert isinstance(result, Movie)
    assert result.title == "Inception"

def test_get_movie_by_title_not_found():
    repo = get_movie_repository()
    repo.clear_db() 
    
    result = repo.get_movie_by_title("Some Unknown Movie")
    assert result is None
