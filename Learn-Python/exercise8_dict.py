phone_book = {"John": "444-222-4444", "Billy": "444-222-1111"}

# get johns number
print(phone_book['John'])

# get billys number
print(phone_book['Billy'])

movies = {"Shawshank Redemption": 9.7, "The God Father": 8.0}


for k in movies.keys():
    print(f"{k} received a score {movies[k]}")


fruit = {
    "banana": 1.00,
    "apple": 1.53,
    "kiwi": 2.00,
    "avocado": 3.23,
    "mango": 2.33,
    "pineapple": 1.44,
    "strawberries": 1.95,
    "melon": 2.34,
    "grapes": 0.98
}

for f in fruit.keys():
    print(f"{f} costs exactly {fruit[f]} with tax.")

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

for p in people.keys():
    print(f"{people[p]['name']} is {people[p]['age']} years old. Sex is {people[p]['sex']}")
