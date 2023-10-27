# TODO: Feature 5 e2e test
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app

def test_edit_movies_page_success(test_app):
    movies = get_movie_repository()
    movies.clear_db()

    edited_movie = movies.create_movie("Interstellar", "Christopher Nolan", 9)
    
    # go to page
    response = test_app.get(f"/movies/{edited_movie.movie_id}")

    assert response.status_code == 200
    assert b"Interstellar" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"9" in response.data

    response = test_app.get(f"/movies/{edited_movie.movie_id}/edit")

    assert response.status_code == 200

    movie_to_be_edited = movies.get_movie_by_title('Interstellar')
    movies.update_movie(movie_to_be_edited.movie_id, 'Jurassic Park', 'Steven Spielberg', 5)

    response = test_app.get(f"/movies/{edited_movie.movie_id}")

    assert response.status_code == 200
    assert b"Jurassic Park" in response.data
    assert b"Steven Spielberg" in response.data
    assert b"5" in response.data

    movies.clear_db()


def test_edit_movies_page_fails(test_app):
    movies = get_movie_repository()
    movies.clear_db()

    edited_movie = movies.create_movie("Interstellar", "Christopher Nolan", 9)
    
    # go to page
    response = test_app.get(f"/movies/{edited_movie.movie_id}")
    assert response.status_code == 200
    assert b"Interstellar" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"9" in response.data

    response = test_app.get(f"/movies/{edited_movie.movie_id}/edit")

    assert response.status_code != 200

    movie_to_be_edited = movies.get_movie_by_title('Interstellar')
    movies.update_movie(movie_to_be_edited.movie_id, 'Jurassic Park', 'Steven Spielberg', 5)

    response = test_app.get(f"/movies/{edited_movie.movie_id}")
    assert response.status_code == 404

    assert b"Jurassic Park" in response.data
    assert b"Steven Spielberg" in response.data
    assert b"5" in response.data

    movies.clear_db()
