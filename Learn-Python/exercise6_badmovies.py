movies = [("Interstellar", 10), ("Ironman", 8.2), ("It Follows", 8.0), ("Idiocracy", 10), ("Mac and Me", 4), ("Superbabies: Baby Geniuses 2", 1.7)]



def filter_movies(movies, filter):
  for m in movies:
    if m[1] > filter:
      print(m)

print(filter_movies(movies, 2))
