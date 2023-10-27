# TODO: Feature 4
import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_view_movie_page(client):
    # use movie in repo
    repo = get_movie_repository()
    repo.clear_db()
    known_movie = repo.create_movie("Inception", "Christopher Nolan", 9)

    # go to page
    response = client.get(f"/movies/{known_movie.movie_id}")

    assert response.status_code == 200
    assert b"Inception" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"9" in response.data
