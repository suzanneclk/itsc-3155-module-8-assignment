from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

movie_ratings = {}

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    py_movies = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', movies=py_movies, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # these variables are fetched from /movies/new
    py_movie = request.form.get('movie')
    py_director = request.form.get('director')
    py_rating = request.form.get('rating')
    if (py_movie != '' and py_director != ''):
        #movie_ratings[movie] = [director, rating] #adds movie to dictionary, with movie name as key
        movie_repository_singleton.create_movie(py_movie, py_director, py_rating) 
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    py_movie = request.args.get('movie-title')
    py_result =  movie_repository_singleton.get_movie_by_title(py_movie)
    return render_template('search_movies.html', search_active=True, py_movie = py_movie, py_result = py_result)