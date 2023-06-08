import requests
from bs4 import BeautifulSoup
import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="movies"
)

# Function to search Google and extract movie details
def get_movie_details(movie_name):
    search_query = f"{movie_name} movie details"
    url = f"https://www.google.com/search?q={search_query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the required information from the search results page
    runtime = soup.select_one("div.BNeawe iBp4i AP7Wnd").text.strip()
    genre = soup.select_one("div.BNeawe div.PZPZlf").text.strip()
    release_year = soup.select_one("div.BNeawe div.Z1hOCe").text.strip()

    return runtime, genre, release_year

# Get user input for movie name
movie_name = input("Enter the movie name: ")

# Retrieve movie details
runtime, genre, release_year = get_movie_details(movie_name)

# Insert the retrieved information into the database
cursor = connection.cursor()
query = "INSERT INTO movies_table (name, runtime, genre, release_year) VALUES (%s, %s, %s, %s)"
values = (movie_name, runtime, genre, release_year)
cursor.execute(query, values)
connection.commit()

# Close the database connection
connection.close()
