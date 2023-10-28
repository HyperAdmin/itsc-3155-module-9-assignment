import pytest
from app import app
from flask import url_for

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_movie_rating_end_to_end(client):
    response = client.get(url_for('create_movie'))
    assert response.status_code == 200

    response = client.post(url_for('create_movie'), data=dict(
        title="Test Movie",
        director="Test Director",
        rating=5
    ), follow_redirects=True)
    assert response.status_code == 200
