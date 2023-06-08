from imdb import Cinemagoer
import mysql.connector
import sys

# Local data
ia = Cinemagoer()

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="movies"
)

def convert_runtime(minutes):
    minutes = eval(minutes)
    hours = minutes // 60  # Integer division to get the number of hours
    minutes = minutes % 60  # Modulo operator to get the remaining minutes

    # Format the hours and minutes into a string
    runtime_string = "{:02d}h {:02d}m".format(hours, minutes)

    return runtime_string


def get_movie_metadata(movie_title):
    # Get movieID
    # get_first_movie exists also
    print("Fetching movie ID...")
    movieid = ia.search_movie(movie_title)[0].movieID

    # Get more info
    print("Requesting metadata...")
    movie = ia.get_movie(movieid)
    if not movie:
        print('No movie found')
        return

    # Get fields you want
    # Each actor contains ['name']. For further inspection pass __dict__ to file
    actors = movie['cast'][:5]

    title = movie['title']
    print(title)

    runtime = movie['runtimes'][0]
    runtime = convert_runtime(runtime)
    print(runtime)

    release_year = movie['year']
    print(release_year)

    # TODO: List is returned
    #director = movie.get('director') returns same thing
    director = movie['director'][0]['name']
    print(director)

    genres = movie['genres'][:3]
    genres_string = ', '.join(genres)
    print(genres_string)

    return title, runtime, release_year, director, genres_string

"""
with open('filename.txt', 'w', encoding="utf-8") as f:
    sys.stdout = f # Change the standard output to the file we created.
    #print(movie.__dict__)
    print(json_object)
"""
"""
counter = 0
# For checking each member of dict
for genre in genres:
    print(genre)
    counter += 1

    if counter == 5:
        break
"""


# Get user input for movie name
while (True):
    movie_name = input("Movie name: ")

    if (movie_name == "."):
        break

    personal_notes = input("Personal thoughts? ")

    # Check if movie is already registered
    movie_found = ia.search_movie(movie_name)[0]['title']

    cursor = connection.cursor()
    query = "SELECT * FROM movies_table WHERE name='"+movie_found+"'" 
    cursor.execute(query)
    # Fetch rows
    rows = cursor.fetchall()
    # Rowcount
    num_rows = cursor.rowcount

    if (num_rows > 0):
        print("Movie " + movie_found + " already exists in registry")
        continue

    # Retrieve movie details
    title, runtime, release_year, director, genre = get_movie_metadata(movie_name)

    # Insert the retrieved information into the database
    # Already existing possibility is handled before
    cursor = connection.cursor()
    query = "INSERT INTO movies_table (name, runtime, release_year, director, notes, genre) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (title, runtime, release_year, director, personal_notes, genre)
    cursor.execute(query, values)
    connection.commit()


# Close cursor and database connection
cursor.close()
connection.close()