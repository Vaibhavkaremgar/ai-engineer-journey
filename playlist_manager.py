movies = ["Inception", "Interstellar", "Tenet"]

print("My movies are: \n")

for movie in movies:
    print(movie)

print(f"Total Movies : {len(movies)}")
new_movie = input("enter your fav movie: ")
movies.append(new_movie)

print("\nLatest Movies are :")

for movie in movies:
    print(movie)

print(f"total movies :- {len(movies)}")



# Challenge 1

# Change songs to your real favorite songs.

# Challenge 2

# Add two songs using two input() calls.

# Challenge 3

# Print:

# Song 1: Roja
# Song 2: Hukum
# ...

songs = ["rojave","chakkani ma annayaku", "uppenatha ee prema"]
print("My fav songs are: ")

for song in songs:
    print(song)

new_song1 = input("enter your latest fav song1: ")
new_song2 = input("enter your latest fav song2: ")
songs.append(new_song1)
songs.append(new_song2)

for index, song in enumerate(songs):
    print(f"Song {index+1}: {song} ")