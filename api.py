from fastapi import FastAPI

from models.movie import load_movies
from models.link import load_links
from models.rating import load_ratings
from models.tag import load_tags

movies_db = "db/movies.csv"
links_db = "db/links.csv"
ratings_db = "db/ratings.csv"
tags_db = "db/tags.csv"

app = FastAPI()


# zad 1
@app.get("/")
def hello_world():
    return {"hello": "world"}


# zad 2
@app.get("/movies")
def get_movies():
    movies = load_movies(movies_db)
    return movies


# zad 3
@app.get("/links")
def get_links():
    links = load_links(links_db)
    return links


@app.get("/ratings")
def get_ratings():
    ratings = load_ratings(ratings_db)
    return ratings


@app.get("/tags")
def get_tags():
    tags = load_tags(tags_db)
    return tags
