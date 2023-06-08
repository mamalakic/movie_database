import requests
from bs4 import BeautifulSoup

#import imdb
import imdb

ia = imdb.Cinemagoer()

def get_movie_metadata(movie_title):
    ia = Cinemagoer.IMDb()
    
    # Search for the movie
    movies = ia.search_movie(movie_title)
    if not movies:
        return None
    
    # Get the first search result (most relevant)
    movie = movies[0]
    ia.update(movie)
    
    # Extract the required metadata
    title = movie.get('title')
    runtime = movie.get('runtime')
    release_year = movie.get('year')
    genre = movie.get('genres')
    
    return title, runtime, release_year, genre

# Provide the movie title
movie_title = "The Shawshank Redemption"

# Call the function to retrieve metadata
metadata = get_movie_metadata(movie_title)

# Display the metadata
if metadata:
    title, runtime, release_year, genre = metadata
    print("Title:", title)
    print("Runtime:", runtime)
    print("Release Year:", release_year)
    print("Genre:", ", ".join(genre))
else:
    print("Movie not found!")