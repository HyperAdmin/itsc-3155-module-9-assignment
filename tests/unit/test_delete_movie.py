# TODO: Feature 6
import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_delete_movie():
    movies=get_movie_repository()
    movies.clear_db()
    movies.create_movie("The Dark Knight", "Christopher Nolan", 5)
    movies.create_movie("Saw X","Kevin Greutert", 4)
    result = movies.get_movie_by_title("Saw X")
    assert isinstance(result, Movie)
    assert result is not None
    assert result.title == "Saw X"
    assert len(movies.get_all_movies())==2
    movies.delete_movie(result.movie_id)
    assert len(movies.get_all_movies())==1
    result = movies.get_movie_by_title("Saw X")
    assert not isinstance(result, Movie)
    movies.clear_db()

def test_deleted_selected_movie():
    movies=get_movie_repository()
    movies.clear_db()
    movies.create_movie("Inception", "Christopher Nolan", 4)
    movies.create_movie("The Shawshank Redemption", "Frank Darabont", 5)
    movies.create_movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 4)
    movies.create_movie("Interstellar", "Christopher Nolan", 4)
    movies.create_movie("The Dark Knight", "Christopher Nolan", 5)
    result = movies.get_movie_by_title("Inception")
    assert len(movies.get_all_movies())==5
    assert isinstance(result, Movie)
    movies.delete_movie(result.movie_id)
    result = movies.get_movie_by_title("Inception")
    assert not isinstance(result, Movie)
    assert len(movies.get_all_movies())==4
    assert result is None
    result = movies.get_movie_by_title("The Dark Knight")
    assert isinstance(result, Movie)
    assert result is not None
    assert result.title=="The Dark Knight"
    result = movies.get_movie_by_title("Interstellar")
    assert isinstance(result, Movie)
    assert result.title=="Interstellar"
    assert result is not None
    result = movies.get_movie_by_title("The Shawshank Redemption")
    assert isinstance(result, Movie)
    assert result.title=="The Shawshank Redemption"
    assert result is not None
    result = movies.get_movie_by_title("The Matrix")
    assert isinstance(result, Movie)
    assert result.title=="The Matrix"
    movies.clear_db()

def test_error():
    movies=get_movie_repository()
    movies.clear_db()
    movies.create_movie("Inception", "Christopher Nolan", 9)
    movies.create_movie("The Shawshank Redemption", "Frank Darabont", 10)
    result = movies.get_movie_by_title("Inception")
    assert result is not None
    try:
        movies.delete_movie(0)
        assert False
    except(ValueError):
        assert True
    movies.clear_db()