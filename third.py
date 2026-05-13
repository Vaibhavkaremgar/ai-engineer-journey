songs = {
    "happy": "Hukum",
    "sad": "Roja",
    "romantic": "Alaipayuthey",
    "motivated": "Hall of Fame"
}

def recommended_songs(mood):
    if mood in songs:
        return songs[mood]
    else:
        return "no recommendation found"
name = input("please enter your name: ")
mood = input("enter your mood: ").lower()

recommend_songs = recommended_songs(mood)

print(f"hello {name} your recommended song is : {recommend_songs}")

songs = songs.append("confused"  "i don't know" )