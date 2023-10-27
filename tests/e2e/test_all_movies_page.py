# TODO: Feature 1
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_list_all_movies(client):
    response = client.get('/movies')

    assert response.status_code == 200

    assert b'All Movies' in response.data
    assert b'See our list of movie ratings below' in response.data
    assert b'Title' in response.data
    assert b'Rating' in response.data

    assert b'Inception' in response.data
    assert b'5' in response.data
    assert b'The Shawshank Redemption' in response.data
    assert b'5' in response.data

if __name__ == '__main__':
    pytest.main()