import pytest
from src.models.movie import Movie

def test_movie_creation():
    movie_id = 65354
    title = "Inception"
    director = "Christopher Nolan"
    rating = 5

    movie = Movie(movie_id, title, director, rating)

    assert movie.movie_id == movie_id
    assert movie.title == title
    assert movie.director == director
    assert movie.rating == rating

if __name__ == '__main__':
    pytest.main()