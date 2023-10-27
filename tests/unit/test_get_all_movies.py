import pytest
from src.models.movie import Movie


class TestMovie(unittest.TestCase):
    def test_movie_creation(self):
        title = "Inception"
        rating = 5

        movie = Movie(title, rating)

        self.assertEqual(movie.title, title)
        self.assertEqual(movie.rating, rating)


if __name__ == "__main__":
    pytest.main()
