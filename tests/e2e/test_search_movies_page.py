# TODO: Feature 3

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_search_movies_page_loads(client):
    url = "/movies/search"
    
    response = client.get(url)
    
    assert response.status_code == 200

    assert b"Search Movie Ratings" in response.data

def test_search_movie_exists(client):
    url = "/movies/search"
    known_movie_title = "Inception"  
    
    response = client.post(url, data={'title': known_movie_title})
    
    assert response.status_code == 200
    assert known_movie_title.encode() in response.data
