from imdb import Cinemagoer
import sys

def convert_runtime(minutes):
    minutes = eval(minutes)
    hours = minutes // 60  # Integer division to get the number of hours
    minutes = minutes % 60  # Modulo operator to get the remaining minutes

    # Format the hours and minutes into a string
    runtime_string = "{:02d}h {:02d}m".format(hours, minutes)

    return runtime_string

# Local data
ia = Cinemagoer()

# Get movieID
# get_first_movie exists also
movieid = ia.search_movie("Oppenheimer")[0].movieID

print("\n\n")

# Get more info
movie = ia.get_movie(movieid)
if not movies:
    print('No movie found')
    return None

# Get fields you want
director = movie['director'][:1]
actors = movie['cast'][:5]
year = movie['year']
runtime = movie['runtimes'][0]
runtime = convert_runtime(runtime)
print(runtime)
genres = movie['genres'][:3]

"""
with open('filename.txt', 'w', encoding="utf-8") as f:
    sys.stdout = f # Change the standard output to the file we created.
    #print(movie.__dict__)
    print(json_object)
"""
# Limit results
counter = 0
# Each actor contains ['name']. For further inspection pass __dict__ to file

# For checking each member of dict
for genre in genres:
    print(genre)
    counter += 1

    if counter == 5:
        break



