from flask import Flask, redirect, render_template, request, abort
from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


def search_movie():
    movie = None
    if request.method == "POST":
        title = request.form["title"]
        movie_repo = get_movie_repository()
        movie = movie_repo.get_movie_by_title(title)

    return render_template("search_movie.html", movie=movie)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/movies")
def list_all_movies():
    # TODO: Feature 1
    movies = movie_repository.get_all_movies()
    return render_template(
        "list_all_movies.html", movies=movies.values(), list_movies_active=True
    )


@app.get("/movies/new")
def create_movies_form():
    return render_template("create_movies_form.html", create_rating_active=True)


@app.post("/movies")
def create_movie():
    # TODO: Feature 2

    title = request.form["title"]
    director = request.form["director"]
    rating = int(request.form["rating"])

    movie = movie_repository.create_movie(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect("/movies")


@app.route("/movies/search", methods=["GET", "POST"])
def search_movies():
    movie = None
    if request.method == "POST":
        title = request.form["title"]
        movie_repo = get_movie_repository()
        movie = movie_repo.get_movie_by_title(title)
    return render_template("search_movies.html", movie=movie, search_active=True)


@app.get("/movies/<int:movie_id>")
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    if not movie:
        return "Movie not found", 404  # Returning a 404 error if movie is not found
    return render_template("get_single_movie.html", movie=movie)


@app.get("/movies/<int:movie_id>/edit")
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template("edit_movies_form.html", movie=movie)


@app.post("/movies/<int:movie_id>")
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    movie = movie_repository.get_movie_by_id(movie_id)
    new_title = request.form["title"]
    new_director = request.form["director"]
    new_rating = int(request.form["rating"])

    edited_movie = movie_repository.update_movie(movie_id, new_title, new_director, new_rating)
    return redirect(f"/movies/{movie_id}")


@app.post("/movies/<int:movie_id>/delete")
def delete_movie(movie_id: int):
    movies=movie_repository.get_all_movies()
    try:
        movie_repository.delete_movie(movie_id)
    except ValueError:
        abort(404)
    
    return redirect("/movies")

if __name__ == "__main__":
    app.run(debug=True)
