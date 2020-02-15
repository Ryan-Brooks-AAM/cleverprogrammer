# movie list example
# list == array
movies = ["Interstellar", "X-Men", "Marley and Me", "Unlimited"]

def display_movies(movies):
    print("Listing movies in library:\n")
    for m in movies:
        print(m)
    print(f"\n{len(movies)} movies in the list/library\n")

# lists can be appended

# display original list
display_movies(movies)

# use append to update lists : list.append("item")
movies.append("The Jetsons")
movies.append("Inception")

print("\nList updated.  Use the append function to update lists.\n")

display_movies(movies)
