# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app
from flask import url_for

def test_delete_movie_page(test_app):
    movies = get_movie_repository()
    movies.clear_db()
    chosen_movie= movies.create_movie("The Dark Knight", "Christopher Nolan", 5)  
    movies.create_movie("Inception", "Christopher Nolan", 4)
    response = test_app.get('/movies')
    assert b"Inception" in response.data
    assert b"5" in response.data
    assert b"The Dark Knight" in response.data
    response = test_app.get(f"/movies/{chosen_movie.movie_id}")
    assert response.status_code == 200
    assert b"The Dark Knight" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"5" in response.data
    response = test_app.post(f'/movies/{chosen_movie.movie_id}/delete')
    assert response.status_code == 302
    response = test_app.post(f'/movies/{0}/delete')
    assert response.status_code == 404
    response = test_app.get('/movies')
    assert b"Inception" in response.data
    assert b"5" in response.data
    movies.clear_db()