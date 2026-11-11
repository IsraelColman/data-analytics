# Description: Creating Collections
# Arthur: Israel Colman

# Movie list
fav_movies = ['Interstellar', 'Dune part 2', 'Warrior']

print(f'The list fav_movies includes my top {len(fav_movies)} favorite movies')

print(fav_movies)

# Using sorted
print(sorted(fav_movies))
print(fav_movies) # I noticed that it sorted the values in alphabetical order.

fav_movies.sort()
print(fav_movies) # I noticed that when using fav_movies it permanetly sorts it alphabetically.
#                   Instead of using print to show it alphabetically now its always sorted alphabetically

fav_movies.append('The Dark Knight')
print(f'The list fav_movies includes my top {len(fav_movies)} favorite movies')