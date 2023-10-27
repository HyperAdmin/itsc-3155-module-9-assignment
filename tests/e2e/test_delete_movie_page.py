# TODO: Feature 6

def test_delete_movie_page(test_app):
    reponse = test_app.get("/movies/{{movie.movie.id}}")

    assert reponse.status_code == 200