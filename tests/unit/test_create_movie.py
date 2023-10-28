import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_movie_rating(client):
    response = client.post('/movies', data=dict(
        title="Test Movie",
        director="Test Director",
        rating=5
    ), follow_redirects=True)

    assert response.status_code == 200  